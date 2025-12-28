#!/usr/bin/env python3
"""
mol-platform CLI Tool

A command-line interface for testing molecular generation capabilities.
"""

import argparse
import json
import sys
from typing import Optional

import requests


def test_health(base_url: str) -> bool:
    """Test the health endpoint."""
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Health check passed: {data}")
            return True
        else:
            print(f"✗ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Health check error: {e}")
        return False


def generate_molecule(
    base_url: str, smiles: str, mutations: int = 3, types: Optional[list] = None
) -> bool:
    """Generate a molecule via API."""
    payload = {
        "base_smiles": smiles,
        "num_mutations": mutations,
        "mutation_types": types or ["substituent", "bond_order", "atom_swap"],
    }

    try:
        response = requests.post(
            f"{base_url}/generate_molecule",
            json=payload,
            headers={"Content-Type": "application/json"},
        )

        if response.status_code == 200:
            data = response.json()
            print("✓ Molecule generation successful")
            print(f"  Original: {data['original_smiles']}")
            print(f"  Generated: {data['generated_smiles']}")
            print(f"  Properties: {json.dumps(data['properties'], indent=2)}")
            return True
        else:
            print(f"✗ Generation failed: {response.status_code}")
            print(f"  Error: {response.text}")
            return False
    except Exception as e:
        print(f"✗ Generation error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="mol-platform CLI - Test molecular generation capabilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py --health
  python cli.py --generate "CC(=O)OC1=CC=CC=C1C(=O)O"
  python cli.py --generate "CCO" --mutations 2 --types substituent atom_swap
        """,
    )

    parser.add_argument(
        "--url",
        default="http://localhost:8000",
        help="Backend API URL (default: http://localhost:8000)",
    )

    parser.add_argument("--health", action="store_true", help="Test health endpoint")

    parser.add_argument(
        "--generate", metavar="SMILES", help="Generate molecule from SMILES string"
    )

    parser.add_argument(
        "--mutations", type=int, default=3, help="Number of mutations (default: 3)"
    )

    parser.add_argument(
        "--types",
        nargs="+",
        choices=["substituent", "bond_order", "atom_swap"],
        default=["substituent", "bond_order", "atom_swap"],
        help="Mutation types to apply",
    )

    args = parser.parse_args()

    if not args.health and not args.generate:
        parser.print_help()
        return 1

    print(f"Connecting to {args.url}")
    print("-" * 50)

    success = True

    if args.health:
        success &= test_health(args.url)

    if args.generate:
        print(f"Generating molecule from: {args.generate}")
        success &= generate_molecule(
            args.url, args.generate, args.mutations, args.types
        )

    print("-" * 50)
    if success:
        print("✓ All tests passed")
        return 0
    else:
        print("✗ Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
