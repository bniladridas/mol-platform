# Command Line Interface

The mol-platform CLI provides command-line access to molecular generation and testing capabilities.

## Overview

The CLI tool (`mol-platform`) allows you to interact with the mol-platform API without the web interface, making it ideal for:

- Automated testing
- Scripting and integration
- Development and debugging
- CI/CD pipelines

## Installation

Build and install the CLI package:

```bash
cd backend
python3 -m venv venv && source venv/bin/activate && pip install build && python -m build
pipx install dist/mol_platform-1.0.0-py3-none-any.whl
```

This installs the `mol-platform` command globally.

## Usage

### Two Modes of Operation

#### 1. Command Mode (Default)

Execute single commands directly:

```bash
mol-platform [OPTIONS] COMMAND
```

#### 2. Interactive Mode

Start an interactive session for multiple commands:

```bash
mol-platform --interactive
```

### Options

- `--url URL`: Backend API URL (default: http://localhost:8000)
- `--interactive, -i`: Start interactive mode
- `--help`: Show help message

### Commands

#### Health Check

Test backend connectivity:

```bash
mol-platform --health
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
mol-platform --generate "SMILES_STRING" [OPTIONS]
```

**Options:**
- `--mutations N`: Number of mutations (default: 3)
- `--types TYPE [TYPE ...]`: Mutation types (substituent, bond_order, atom_swap)

**Examples:**

```bash
# Basic generation
mol-platform --generate "CCO"

# Custom mutations
mol-platform --generate "CC(=O)OC1=CC=CC=C1C(=O)O" --mutations 2

# Specific mutation types
mol-platform --generate "CCO" --types substituent
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

#### Interactive Mode

Start interactive session:

```bash
mol-platform --interactive
```

**Interactive Commands:**
```
mol-platform> help
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
```

**Interactive Session Example:**
```
🧬 mol-platform Interactive CLI
Connected to: http://localhost:8000
Type 'help' for commands, 'quit' to exit
--------------------------------------------------
mol-platform> set mutations 5
✓ Mutations set to 5
mol-platform> generate CCO
Generating molecule from: CCO
✓ Molecule generation successful
  Original: CCO
  Generated: CC(C)(C)O
  Properties: {...}
mol-platform> status
API URL: http://localhost:8000
Mutations: 5
Types: ['substituent', 'bond_order', 'atom_swap']
mol-platform> quit
Goodbye! 👋
```

### Options

- `--url URL`: Backend API URL (default: http://localhost:8000)
- `--help`: Show help message

### Commands

#### Health Check

Test backend connectivity:

```bash
mol-platform --health
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
mol-platform --generate "SMILES_STRING" [OPTIONS]
```

**Options:**
- `--mutations N`: Number of mutations (default: 3)
- `--types TYPE [TYPE ...]`: Mutation types (substituent, bond_order, atom_swap)

**Examples:**

```bash
# Basic generation
mol-platform --generate "CCO"

# Custom mutations
mol-platform --generate "CC(=O)OC1=CC=CC=C1C(=O)O" --mutations 2

# Specific mutation types
mol-platform --generate "CCO" --types substituent atom_swap
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
    mol-platform --health
    mol-platform --generate "CCO"
```

### Scripting

```python
import subprocess

# Health check
result = subprocess.run(["mol-platform", "--health"], capture_output=True)
print("Exit code:", result.returncode)

# Generation
result = subprocess.run([
    "mol-platform", "--generate", "CCO", "--mutations", "1"
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
   - Ensure the package is installed correctly with pipx

### Debug Mode

For detailed error information, check the backend server logs while running CLI commands.