

# Copilot Instructions for AI Agents

## Project Overview
This repository implements a modular Python backend (see `backend/`) for service-oriented workflows, with a FastAPI entrypoint (`backend/app/main.py`). The architecture enforces strict separation between API endpoints, business logic, and integrations. A minimal frontend exists in `frontend/` for static assets and demos.

## Architecture & Data Flow
- **API Layer** (`backend/app/api/`): HTTP endpoints, message queue (RabbitMQ/Redis) consumers/producers, document-to-signal, RSS scraping, and response templating. Each integration (e.g., `consume_*.py`, `push_*.py`) is isolated and modular.
- **Core Logic** (`backend/app/core/`): Business logic (question analysis, search, response templating, etc). API handlers delegate to these modules; do not mix API and business logic.
- **RAG Engine** (`backend/app/rag/engine.py`): Retrieval-augmented generation for advanced search/response.
- **Templates** (`backend/app/templates/`): Jinja2 HTML templates for all web output.

**Data Flow:**
1. API endpoints (HTTP or queue) handled in `api/`.
2. Handlers call `core/` modules for processing.
3. Signals/documents may be routed to queues or templates.
4. RAG engine is used for complex retrieval.

## Developer Workflows
- **Run the API:**
  - `uvicorn backend.app.main:app --reload` (use `.venv` if available)
  - FastAPI docs: `/docs` (when running)
- **Minimal API:** Use `minimal_api.py` for lightweight endpoints.
- **Testing:** No standard suite; add tests under `tests/` if needed.
- **Debugging:** Use FastAPI docs, logs, and minimal API for troubleshooting.

## Project-Specific Conventions
- **Separation of Concerns:** API logic (`api/`) is strictly separated from business logic (`core/`).
- **Integration Patterns:**
  - Message queue: modular, see `consume_*.py`, `push_*.py` (RabbitMQ/Redis)
  - Document-to-signal and RSS scraping: dedicated modules
- **Explicit Imports:** No wildcard imports; always use explicit imports.
- **HTML Output:** All web output uses Jinja2 templates in `templates/`.
- **Route Registration:** Register new API routes in `main.py` or `minimal_api.py`.

## Integration Points
- **RabbitMQ/Redis:** For async messaging/persistence (`consume_*.py`, `push_*.py`)
- **RSS Feeds:** Scraped/processed for signals (`rss_scraper.py`)
- **RAG Engine:** Advanced retrieval/response (`rag/engine.py`)

## Examples
- **Add API Route:**
  1. Create handler in `backend/app/api/`
  2. Register in `main.py` or `minimal_api.py`
- **Add Business Logic:**
  1. Implement in `core/`
  2. Call from API handler

## References
- `backend/app/api/`: Integration patterns
- `backend/app/core/`: Business logic structure
- `backend/app/rag/engine.py`: RAG integration

---
For questions, follow the structure and patterns in the referenced files. Keep new code modular and consistent. If conventions or workflows are unclear, ask for clarification or examples.
