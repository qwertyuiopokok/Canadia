#!/bin/bash

set -e  # Exit on error

PORT=9800
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🔎 Nettoyage du port $PORT..."
lsof -ti tcp:"$PORT" | xargs kill -9 2>/dev/null || true

cd "$SCRIPT_DIR"

echo "🔧 Vérification de l'environnement virtuel..."
if [ ! -d ".venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv .venv
fi

echo "📥 Installation/Mise à jour des dépendances..."
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    .venv/bin/pip install --quiet -r "$SCRIPT_DIR/requirements.txt" || {
        echo "⚠️  Erreur lors de l'installation des dépendances"
    }
else
    .venv/bin/pip install --quiet \
        fastapi uvicorn python-dotenv pydantic pydantic-settings \
        langchain langchain-community langchain-core \
        feedparser requests jinja2 sqlalchemy \
        aiohttp openai pika redis beautifulsoup4
fi

echo "🚀 Lancement de Canadia sur le port $PORT..."

# Change to backend directory for proper imports
cd "$SCRIPT_DIR/backend"

# Try venv first, fallback to system python
if [ -f "$SCRIPT_DIR/.venv/bin/uvicorn" ]; then
    "$SCRIPT_DIR/.venv/bin/uvicorn" app.main:app --host 127.0.0.1 --port "$PORT"
else
    python3 -m uvicorn app.main:app --host 127.0.0.1 --port "$PORT"
fi
