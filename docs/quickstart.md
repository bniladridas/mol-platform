# Quick Start

Get mol-platform up and running quickly with Docker.

## Docker Deployment (Recommended)

1. **Start the services:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   - **Frontend:** http://localhost:3000
   - **API Documentation:** http://localhost:8000/docs
   - **API Health:** http://localhost:8000/health

3. **Stop the services:**
   ```bash
   docker-compose down
   ```

## Local Development

### Backend
```bash
cd backend
source venv/bin/activate
python src/main.py
```
API available at http://localhost:8000

### Frontend
```bash
cd frontend
npm start
```
Frontend available at http://localhost:3000

## Testing

Run the test suite:
```bash
# Backend tests
cd backend
python -m pytest tests/ -v

# Frontend tests
cd frontend
npm test
```

## What's Next?

- [API Documentation](../api/overview.md)
- [Configuration](configuration.md)
- [Contributing](../contributing.md)