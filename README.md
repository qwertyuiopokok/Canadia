# Canadia - Canadian Information Search Engine

## Quick Start

To start the Canadia server, simply run:

```bash
./start_canadia.sh
```

The server will start on `http://127.0.0.1:9800`

## What the script does

1. Cleans up any existing process on port 9800
2. Activates the Python virtual environment from `backend/.venv`
3. Sets up the Python path to include the backend directory
4. Starts the FastAPI/Uvicorn server

## Available Endpoints

- `/` - Main search interface (HTML)
- `/status` - Health check endpoint
- `/monitor/memory` - Memory usage monitoring
- `/ask` - Question answering endpoint
- `/charte` - Charter page
- `/signals/html` - Signals page

## Development Setup

If you need to recreate the environment:

1. Remove old virtual environment (if exists):
   ```bash
   rm -rf backend/.venv
   ```

2. Create new virtual environment:
   ```bash
   cd backend
   python3 -m venv .venv
   ```

3. Install dependencies:
   ```bash
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. Start the server:
   ```bash
   cd ..
   ./start_canadia.sh
   ```

## Requirements

- Python 3.9+
- All Python dependencies are listed in `backend/requirements.txt`

## Architecture

- **Backend**: FastAPI application in `backend/app/`
- **Frontend**: Static HTML templates in `backend/app/templates/`
- **API Routes**: Modular routers in `backend/app/api/`
- **Core Logic**: Business logic in `backend/app/core/`

## Notes

- The virtual environment is stored in `backend/.venv` and is excluded from git
- The server uses port 9800 by default (configurable in `start_canadia.sh`)
