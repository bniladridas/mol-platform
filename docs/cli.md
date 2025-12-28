# Command Line Interface

The mol-platform CLI provides command-line access to molecular generation and testing capabilities.

## Overview

The CLI tool (`cli.py`) allows you to interact with the mol-platform API without the web interface, making it ideal for:

- Automated testing
- Scripting and integration
- Development and debugging
- CI/CD pipelines

## Installation

No additional installation required. The CLI is included with the codebase.

## Usage

### Basic Syntax

```bash
python cli.py [OPTIONS] COMMAND
```

### Options

- `--url URL`: Backend API URL (default: http://localhost:8000)
- `--help`: Show help message

### Commands

#### Health Check

Test backend connectivity:

```bash
python cli.py --health
```

**Output:**
```
Connecting to http://localhost:8000
--------------------------------------------------
✓ Health check passed: {'status': 'healthy', 'version': '1.0.0'}
--------------------------------------------------
✓ All tests passed
```

#### Molecule Generation

Generate molecules with mutations:

```bash
python cli.py --generate "SMILES_STRING" [OPTIONS]
```

**Options:**
- `--mutations N`: Number of mutations (default: 3)
- `--types TYPE [TYPE ...]`: Mutation types (substituent, bond_order, atom_swap)

**Examples:**

```bash
# Basic generation
python cli.py --generate "CCO"

# Custom mutations
python cli.py --generate "CC(=O)OC1=CC=CC=C1C(=O)O" --mutations 2

# Specific mutation types
python cli.py --generate "CCO" --types substituent atom_swap
```

**Sample Output:**
```
Connecting to http://localhost:8000
--------------------------------------------------
Generating molecule from: CCO
✓ Molecule generation successful
  Original: CCO
  Generated: CC(C)O
  Properties: {
    "Molecular Weight": 46.07,
    "LogP": 0.16,
    "H-Bond Donors": 1,
    "H-Bond Acceptors": 1,
    "Topological Polar Surface Area": 20.2
  }
--------------------------------------------------
✓ All tests passed
```

## Prerequisites

- Python 3.12+
- Running mol-platform backend server
- `requests` library (included in backend environment)

## Error Handling

The CLI provides clear error messages:

- **Connection Errors:** When backend is not accessible
- **Validation Errors:** For invalid SMILES or parameters
- **API Errors:** Server-side processing failures

## Integration

### CI/CD Usage

```yaml
- name: Test CLI
  run: |
    python cli.py --health
    python cli.py --generate "CCO"
```

### Scripting

```python
import subprocess

# Health check
result = subprocess.run(["python", "cli.py", "--health"], capture_output=True)
print("Exit code:", result.returncode)

# Generation
result = subprocess.run([
    "python", "cli.py", "--generate", "CCO", "--mutations", "1"
], capture_output=True)
print("Output:", result.stdout.decode())
```

## Troubleshooting

### Common Issues

1. **Connection Refused**
   - Ensure backend server is running on localhost:8000
   - Check firewall settings

2. **Invalid SMILES**
   - Verify SMILES string is valid
   - Use tools like ChemDraw for validation

3. **Permission Errors**
   - Ensure execute permissions: `chmod +x cli.py`

### Debug Mode

For detailed error information, check the backend server logs while running CLI commands.