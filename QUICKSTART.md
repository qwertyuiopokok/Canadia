# Quick Start Guide - Canadia Development Environment

This guide will help you set up the Canadia development environment on your local machine.

## Prerequisites

- Python 3.9 or higher
- macOS, Linux, or Windows

## Setup Steps

### 1. Clone the Repository (if not already done)

```bash
git clone https://github.com/qwertyuiopokok/Canadia.git
cd Canadia
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate Virtual Environment

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```cmd
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt.

### 4. Upgrade pip

```bash
pip install --upgrade pip
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- FastAPI (web framework)
- Uvicorn (ASGI server)
- LangChain (LLM framework)
- FAISS (vector search)
- And many more dependencies

### 6. Configure Environment Variables

Copy the example `.env` file (if exists) or create one:

```bash
# Create .env file with your configuration
# Example:
# API_KEY=your_api_key_here
```

### 7. Start the Development Server

**Using the startup script (recommended):**
```bash
./start_canadia.sh
```

**Or manually:**
```bash
source .venv/bin/activate
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 9800
```

### 8. Access the Application

- API: http://localhost:9800 (or http://[your-server-ip]:9800 for remote access)
- API Documentation (Swagger UI): http://localhost:9800/docs
- Alternative Documentation (ReDoc): http://localhost:9800/redoc

## Verification

To verify your installation:

```bash
# Check Python version
python3 --version

# Check uvicorn is installed
.venv/bin/uvicorn --version

# Check pip packages
pip list
```

## Common Issues

### Issue: "uvicorn: command not found"

**Solution:** Make sure the virtual environment is activated:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### Issue: "Port already in use"

**Solution:** Kill the process using the port:
```bash
# macOS/Linux
lsof -ti tcp:9800 | xargs kill -9

# Windows
netstat -ano | findstr :9800
taskkill /PID <PID> /F
```

### Issue: Import errors when running uvicorn

**Solution:** Make sure you're in the virtual environment and running from the `backend` directory:
```bash
source .venv/bin/activate  # From root directory
cd backend
uvicorn app.main:app --reload
```

### Issue: "Connection refused" or cannot access the site

**Solutions:**
1. **Install all dependencies first:**
   ```bash
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Use correct host binding:** Server must use `0.0.0.0` to accept external connections (already configured in `start_canadia.sh`)
3. **Access from correct URL:**
   - Local: http://localhost:9800
   - Remote: http://[server-ip]:9800
4. **Check firewall settings:** Ensure port 9800 is not blocked

### Issue: ModuleNotFoundError

**Solution:** Dependencies not installed. Run:
```bash
pip install -r requirements.txt
```

## Development Workflow

1. **Activate environment:** `source .venv/bin/activate`
2. **Make changes** to code
3. **Test locally:** Server auto-reloads with `--reload` flag
4. **Check API docs:** Visit http://localhost:9800/docs
5. **Commit changes:** Use git as normal

## Deactivating the Virtual Environment

When you're done:

```bash
deactivate
```

## Next Steps

- Read the full [README.md](README.md) for architecture details
- Explore the API at http://localhost:9800/docs
- Check the `backend/app/` directory for code structure
- Review endpoints in `backend/app/api/`

---

**Note:** The `.venv` directory is not tracked by git. Each developer needs to create their own virtual environment locally.
