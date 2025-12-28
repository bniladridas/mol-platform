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


class CLISession:
    """CLI session state manager."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.mutations = 3
        self.types = ["substituent", "bond_order", "atom_swap"]


def test_health(base_url: str, api_key: str) -> bool:
    """Test the health endpoint."""
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(f"{base_url}/health", headers=headers)
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
    base_url: str,
    api_key: str,
    smiles: str,
    mutations: int = 3,
    types: Optional[list] = None,
) -> bool:
    """Generate a molecule via API."""
    payload = {
        "base_smiles": smiles,
        "num_mutations": mutations,
        "mutation_types": types or ["substituent", "bond_order", "atom_swap"],
    }

    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        response = requests.post(
            f"{base_url}/generate_molecule",
            json=payload,
            headers=headers,
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


def interactive_mode(base_url: str, api_key: str):
    """Run interactive CLI mode."""
    session = CLISession(api_key)

    print("🧬 mol-platform Interactive CLI")
    print(f"Connected to: {base_url}")
    print("Type 'help' for commands, 'quit' to exit")
    print("-" * 50)

    while True:
        try:
            cmd = input("mol-platform> ").strip()

            if not cmd:
                continue

            if cmd.lower() in ["quit", "exit", "q"]:
                print("Goodbye! 👋")
                break

            if cmd.lower() == "help":
                print(
                    """
Available commands:
  health              - Test API health
  generate <smiles>   - Generate molecule from SMILES
  set mutations <n>   - Set number of mutations (default: 3)
  set types <types>   - Set mutation types (substituent bond_order atom_swap)
  status              - Show current settings
  clear               - Clear screen
  help                - Show this help
  quit                - Exit interactive mode

Examples:
  generate CCO
  set mutations 5
  set types substituent atom_swap
  health
                """.strip()
                )
                continue

            if cmd.lower() == "clear":
                print("\033[2J\033[H", end="")  # Clear screen
                continue

            if cmd.lower() == "status":
                print(f"API URL: {base_url}")
                print(f"Mutations: {session.mutations}")
                print(f"Types: {session.types}")
                continue

            parts = cmd.split()
            command = parts[0].lower()

            if command == "health":
                test_health(base_url, session.api_key)

            elif command == "generate":
                if len(parts) < 2:
                    print("❌ Error: Please provide SMILES string")
                    print("Example: generate CCO")
                    continue
                smiles = parts[1]
                print(f"Generating molecule from: {smiles}")
                generate_molecule(
                    base_url, session.api_key, smiles, session.mutations, session.types
                )

            elif command == "set":
                if len(parts) < 3:
                    print("❌ Error: Invalid set command")
                    print(
                        "Usage: set mutations <number> OR set types <type1> <type2> ..."
                    )
                    continue

                subcommand = parts[1].lower()
                if subcommand == "mutations":
                    try:
                        n = int(parts[2])
                        if n < 0:
                            print("❌ Error: Mutations must be non-negative")
                        else:
                            session.mutations = n
                            print(f"✓ Mutations set to {n}")
                    except ValueError:
                        print("❌ Error: Invalid number")
                elif subcommand == "types":
                    types = parts[2:]
                    valid_types = ["substituent", "bond_order", "atom_swap"]
                    invalid = [t for t in types if t not in valid_types]
                    if invalid:
                        print(f"❌ Error: Invalid types: {invalid}")
                        print(f"Valid types: {valid_types}")
                    else:
                        session.types = types
                        print(f"✓ Types set to: {types}")
                else:
                    print("❌ Error: Unknown setting. Use 'mutations' or 'types'")
            else:
                print(f"❌ Unknown command: {command}")
                print("Type 'help' for available commands")

        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except EOFError:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="mol-platform CLI - Test molecular generation capabilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  mol-platform --api-key your-key --health
  mol-platform --api-key your-key --generate "CC(=O)OC1=CC=CC=C1C(=O)O"
  mol-platform --api-key your-key --interactive

Interactive mode:
  mol-platform --api-key your-key --interactive
  Then type commands like: generate CCO, set mutations 5, health, etc.
        """,
    )

    parser.add_argument(
        "--url",
        default="http://localhost:8000",
        help="Backend API URL (default: http://localhost:8000)",
    )

    parser.add_argument(
        "--api-key",
        required=True,
        help="API key for authentication",
    )

    parser.add_argument(
        "--interactive", "-i", action="store_true", help="Start interactive mode"
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

    if args.interactive:
        interactive_mode(args.url, args.api_key)
        return 0

    if not args.health and not args.generate:
        parser.print_help()
        return 1

    print(f"Connecting to {args.url}")
    print("-" * 50)

    success = True

    if args.health:
        success &= test_health(args.url, args.api_key)

    if args.generate:
        print(f"Generating molecule from: {args.generate}")
        success &= generate_molecule(
            args.url, args.api_key, args.generate, args.mutations, args.types
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
