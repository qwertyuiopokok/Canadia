# Canadia

A FastAPI-based backend platform with RAG (Retrieval-Augmented Generation) capabilities for processing news and providing intelligent responses.

## Project Structure

```
Canadia/
├── backend/            # Backend Python code
│   ├── app/           # Main application code
│   │   ├── api/       # API endpoints
│   │   ├── core/      # Business logic
│   │   ├── rag/       # RAG engine
│   │   └── main.py    # FastAPI application entry point
│   └── __init__.py
├── docs/              # Documentation and frontend demos
├── .venv/             # Python virtual environment (not committed)
├── requirements.txt   # Python dependencies
└── start_canadia.sh   # Startup script
```

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### 1. Create Virtual Environment

From the root Canadia directory:

```bash
python3 -m venv .venv
```

### 2. Activate Virtual Environment

**macOS/Linux (bash/zsh):**
```bash
source .venv/bin/activate
```

**Windows:**
```cmd
.venv\Scripts\activate
```

After activation, your prompt should show `(.venv)` prefix.

### 3. Upgrade pip

```bash
pip install --upgrade pip
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- FastAPI and Uvicorn (web framework and ASGI server)
- LangChain and RAG dependencies (langchain, faiss-cpu, sentence-transformers)
- Database and storage (SQLAlchemy, Redis, Pika)
- Web scraping tools (BeautifulSoup4, feedparser)
- And other required packages

### 5. Environment Configuration

Create a `.env` file in the root directory with your configuration:

```bash
# Example .env configuration
# Add your API keys and configuration here
```

### 6. Run the Application

**Option A: Using the startup script (recommended)**
```bash
./start_canadia.sh
```

**Option B: Manual startup**
```bash
source .venv/bin/activate
cd backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 9800
```

The API will be available at:
- Main API: http://127.0.0.1:9800
- Swagger UI docs: http://127.0.0.1:9800/docs
- ReDoc: http://127.0.0.1:9800/redoc

## Development

### Verify Installation

Check that uvicorn is properly installed:
```bash
.venv/bin/uvicorn --version
which .venv/bin/uvicorn
```

### Running in Development Mode

For development with auto-reload:
```bash
source .venv/bin/activate
cd backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 9800
```

### Project Architecture

The application follows a modular architecture:

- **API Layer** (`backend/app/api/`): HTTP endpoints and integrations
- **Core Logic** (`backend/app/core/`): Business logic and processing
- **RAG Engine** (`backend/app/rag/`): Vector search and retrieval
- **Templates** (`backend/app/templates/`): Jinja2 HTML templates

## Key Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server with performance optimizations
- **LangChain**: Framework for LLM applications
- **FAISS**: Vector similarity search
- **Sentence Transformers**: Text embeddings
- **BeautifulSoup4**: Web scraping and parsing
- **Pika**: RabbitMQ client for message queuing
- **Redis**: Caching and data persistence

## Troubleshooting

### uvicorn command not found

Make sure you've activated the virtual environment:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### Import errors

Ensure you're in the virtual environment and running from the `backend` directory:
```bash
source .venv/bin/activate  # From root directory
cd backend
uvicorn app.main:app --reload
```

### Port already in use

Kill the process using the port (default 9800):
```bash
lsof -ti tcp:9800 | xargs kill -9  # macOS/Linux
```

## License

[Add license information here]
