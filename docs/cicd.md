# CI/CD

Continuous Integration and Deployment pipeline for mol-platform.

## GitHub Actions Workflows

### CI Workflow (.github/workflows/ci.yml)

Runs on pushes and PRs to main:

1. **Setup Environment**
   - Python 3.12
   - Node.js 18

2. **Backend Testing**
   - Install dependencies
   - Run unit tests
   - Run e2e tests

3. **Frontend Testing**
   - Install dependencies
   - Run unit tests
   - Run linting

4. **Build Check**
   - Build Docker images

### Docker Workflow (.github/workflows/docker.yml)

Builds and pushes Docker images to GitHub Container Registry:

- Triggered on pushes and PRs
- Builds backend, frontend, and celery images
- Pushes to `ghcr.io`

### E2E Workflow (.github/workflows/e2e.yml)

Full end-to-end testing:

- Builds Docker containers
- Starts services
- Runs Cypress e2e tests
- Manual trigger available

## Pre-commit Hooks

Local quality checks using pre-commit:

- Ruff linting and formatting
- Commit message validation

Install:
```bash
pip install pre-commit
pre-commit install
```

## Quality Gates

### Code Quality
- **Linting:** Ruff (Python)
- **Formatting:** Ruff format
- **Type checking:** Basic validation

### Testing
- **Unit tests:** pytest
- **E2E tests:** Cypress
- **Coverage:** Not enforced but monitored

### Security
- **Dependencies:** Automated scanning
- **Vulnerabilities:** npm audit, pip security

## Deployment

### Manual Deployment

```bash
# Build images
docker-compose build

# Deploy
docker-compose up -d
```

### Automated Deployment

Configure your platform (Heroku, AWS, etc.) to:
1. Pull images from GitHub Container Registry
2. Use docker-compose.yml for orchestration
3. Set environment variables from secrets

## Monitoring

- Health check endpoint: `GET /health`
- Application logs in Docker
- GitHub Actions run history