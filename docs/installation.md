# Installation

This guide covers how to install and set up mol-platform for development and deployment.

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

## Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bniladridas/mol-platform.git
   cd mol-platform
   ```

2. **For Docker deployment (recommended):**
   No additional installation required. Everything runs in containers.

3. **For local development:**
   ```bash
   # Backend setup
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python src/main.py  # Start backend server

   # Frontend setup (in separate terminal)
   cd ../frontend
   npm install
   npx react-scripts start  # Start frontend development server
   ```

## Next Steps

- [Quick Start Guide](quickstart.md)
- [Configuration](configuration.md)