# Molecular Design Platform

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