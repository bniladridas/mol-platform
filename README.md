# mol-platform

A containerized microservice for molecular analysis, simulation, and visualization. Developed with consideration for reproducibility, modularity, and scalability through Docker.

---

## Prerequisites

### Required (All Platforms)

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/)

### Recommended (macOS via Homebrew)

If you are developing or running tests locally on macOS, install the following using **Homebrew**:

```bash
brew install docker docker-compose
brew install python@3.12
brew install node
brew install git
```

Ensure Homebrew itself is installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify versions:

```bash
docker --version
docker-compose --version
python3 --version
node --version
```

---

## Execution

To initiate the platform:

```bash
docker-compose up --build
```

## Local Development

For development purposes without containerization:

### Backend Configuration
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

### Frontend Configuration
```bash
cd frontend
npm install
npx react-scripts start
```

## Access Points

- **API Documentation:** http://localhost:8000/docs
- **Frontend Interface:** http://localhost:3000

---

## API Reference

### Molecule Generation

**Endpoint:** `POST /generate_molecule`

Facilitates the creation of molecular variants through systematic mutations.

**Request Structure**

```json
{
  "base_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
  "num_mutations": 3,
  "mutation_types": ["substituent", "bond_order", "atom_swap"]
}
```

**Parameters:**
- `base_smiles`: SMILES representation (required)
- `num_mutations`: Mutation count (optional, default: 3)
- `mutation_types`: Permitted mutation categories (optional)

**Response Structure:**
```json
{
  "original_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
  "generated_smiles": "CC(=O)Oc1cSCN)cccc1C(=O)O",
  "molecular_image": "base64_encoded_png",
  "properties": {
    "Molecular Weight": 180.16,
    "LogP": 1.31,
    "H-Bond Donors": 1,
    "H-Bond Acceptors": 3,
    "Topological Polar Surface Area": 63.6
  }
}
```

**Available Mutations:**
- `substituent`: Introduces substituent groups
- `bond_order`: Adjusts bonding configurations
- `atom_swap`: Exchanges atomic elements

### Health Verification

**Endpoint:** `GET /health`

Provides service status confirmation.

**Response Structure:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

**Response**

```json
{
  "original_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
  "generated_smiles": "CC(=O)OC1=CC=CC=C1C(=O)OC",
  "molecular_image": "base64_encoded_png",
  "properties": {
    "Molecular Weight": 180.16,
    "LogP": 1.31,
    "H-Bond Donors": 1,
    "H-Bond Acceptors": 3,
    "Topological Polar Surface Area": 63.6
  }
}
```

---

### Health Check

**Endpoint:** `GET /health`

```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

## Testing

> These steps are **optional** if you only use Docker. They are recommended for contributors and CI parity.

### Backend Unit Tests (Local)

```bash
brew install python@3.12
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python -m pytest backend/tests/ -v
```

### Frontend Unit Tests (Local)

```bash
brew install node
cd frontend
npm install
npm test
```

---

### E2E Tests (Local)

```bash
# Start services
docker-compose up -d

# Backend E2E
cd backend
python -m pytest tests/e2e/ -v

# Frontend E2E
cd frontend
npm run cypress:run
```

---

## CI/CD

This project uses **GitHub Actions** with Docker-based workflows:

* **CI Workflow** (`ci.yml`)
  Runs unit tests (backend + frontend), builds images, and checks quality.

* **Docker Workflow** (`docker.yml`)
  Builds and publishes images to GitHub Container Registry.

* **E2E Workflow** (`e2e.yml`)
  Spins up the full stack and runs end-to-end tests.

* **Dependabot**
  Weekly updates for pip, npm, and Docker dependencies.

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/backend"
    schedule:
      interval: "weekly"
  - package-ecosystem: "npm"
    directory: "/frontend"
    schedule:
      interval: "weekly"
  - package-ecosystem: "docker"
    directory: "backend"
    schedule:
      interval: "weekly"
  - package-ecosystem: "docker"
    directory: "frontend"
    schedule:
      interval: "weekly"
```

---

## Troubleshooting

### RDKit Import Error (macOS / Local Dev)

If running RDKit locally (outside Docker):

```bash
brew install rdkit
brew install cairo
brew install boost
```

Ensure Python can see RDKit:

```bash
python3 -c "from rdkit import Chem; print(Chem.__version__)"
```

### RDKit Import Error (Docker / Celery)

If the Celery service fails due to RDKit imports, ensure this is present in the Dockerfile:

```bash
apt-get install -y libxext6
```

Then rebuild:

```bash
docker-compose up --build
```

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Run tests locally or via Docker
4. Open a pull request

---

## Technical Notes

* Molecule mutations now use `random.choice` for safer, type-consistent selection.
* Docker is the **source of truth** for runtime environments.
* Homebrew is recommended only for local development and debugging.

---

## Commit Convention

This project follows **Conventional Commits**.

### Setup (Local)

```bash
cp scripts/commit-msg .git/hooks/
chmod +x .git/hooks/commit-msg
```

### Rules

* Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`, `revert`
* Lowercase
* ≤ 60 characters

**Example**

```bash
feat: add new molecule visualization
```

### Rewriting Commits

```bash
bash scripts/rewrite_msg.sh "<new-message>"
```

Use `git filter-branch` for bulk rewrites (with caution).