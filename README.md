# mol-platform

A **containerized microservice application** for molecular simulation, mutation analysis, and visualization — designed for reproducibility, modularity, and scalability using Docker.

## Prerequisites

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Run the Platform

```bash
docker-compose up --build
```

## Access Points

* **API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Frontend Interface:** [http://localhost:3000](http://localhost:3000)

## API Endpoints

### Generate Molecule
**Endpoint:** `POST /generate_molecule`

Generates a new molecule by applying random mutations to a base molecule.

**Request Body:**
```json
{
  "base_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
  "num_mutations": 3,
  "mutation_types": ["substituent", "bond_order", "atom_swap"]
}
```

**Response:**
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

### Health Check
**Endpoint:** `GET /health`

Returns the health status of the service.

**Response:**
```json
{
  "status": "healthy"
}
```

## Testing

### Unit Tests

Run backend unit tests:
```bash
cd backend
pip install -r requirements.txt
python -m pytest tests/ -v
```

Run frontend unit tests:
```bash
cd frontend
npm install
npm test
```

### E2E Tests

Run full-stack e2e tests locally:
```bash
# Start services
docker-compose up -d

# Run backend e2e
cd backend
python -m pytest tests/e2e/ -v

# Run frontend e2e
cd frontend
npm run cypress:run
```

### CI/CD

- **CI Workflow**: Runs unit tests and builds Docker images on pushes/PRs.
- **Docker Workflow**: Builds and pushes images to GHCR on pushes/PRs.
- **E2E Workflow**: Runs full e2e tests on pushes (can be triggered manually).

## Troubleshooting

**RDKit Import Error**

If the Celery service fails to start due to an RDKit import error, ensure that `libxext6` is installed in the Celery Dockerfile.

```bash
apt-get install -y libxext6
```

Rebuild or restart the containers to apply the fix:

```bash
docker-compose up --build
# or
docker-compose restart
```

After this update, all platform services should start successfully.

## Contributing

Contributions are encouraged.
Please open an issue or submit a pull request for review.

## Commit Convention

This project follows the **Conventional Commits** specification.

### Setup

To enable local commit message validation:

```bash
cp scripts/commit-msg .git/hooks/
chmod +x .git/hooks/commit-msg
```

### Format Rules

* Begin with a type: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`, `revert`
* Use lowercase
* Keep the summary ≤ 60 characters

Example:

```bash
feat: add new molecule visualization
```

### Rewriting Commits

To rewrite a specific commit message:

```bash
bash scripts/rewrite_msg.sh "<new-message>"
```

Use `git filter-branch` for bulk message rewrites (with caution).