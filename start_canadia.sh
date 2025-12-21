#!/bin/bash

PORT=8000

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if virtual environment exists, if not create it
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv "$SCRIPT_DIR/.venv"
    
    echo "📥 Installation des dépendances..."
    "$SCRIPT_DIR/.venv/bin/pip" install -q fastapi uvicorn python-dotenv jinja2 requests feedparser beautifulsoup4 lxml langchain langchain-community
    echo "✅ Environnement configuré avec succès!"
fi

echo "🔎 Nettoyage du port $PORT..."
lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null

echo "🚀 Lancement de Canadia sur le port $PORT..."
cd "$SCRIPT_DIR/backend"
"$SCRIPT_DIR/.venv/bin/python3" -m uvicorn app.main:app --host 127.0.0.1 --port $PORT
