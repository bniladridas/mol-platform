# Molecular Design Platform

A containerized application for molecular simulation and mutation analysis using microservices architecture with Docker.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Running the Platform
```sh
docker-compose up --build
```

## Accessing the Platform
- **Backend API**: http://localhost:8000/docs
- **Frontend**: http://localhost:3000

## Contributing
Contributions are welcome! Submit issues or pull requests.

## Conventional Commits

This project uses conventional commit standards for commit messages.

### Setup

To enable commit message validation, copy the hook to your local git hooks:

```sh
cp scripts/commit-msg .git/hooks/
chmod +x .git/hooks/commit-msg
```

### Standards

Commit messages must:
- Start with a type: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`, `revert`
- Be lowercase
- Be ≤ 60 characters for the first line

Example: `feat: add new molecule visualization`

### Rewriting History

To rewrite existing commit messages, use the provided script:

```sh
bash scripts/rewrite_msg.sh <commit-message>
```

For bulk rewriting, use git filter-branch (use with caution).

## License
This project is licensed under the MIT License.
