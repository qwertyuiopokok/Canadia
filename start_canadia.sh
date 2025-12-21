#!/bin/bash

PORT=8000

echo "🔎 Nettoyage du port $PORT..."
lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null

echo "🚀 Lancement de Canadia sur le port $PORT..."
# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/backend"
"$SCRIPT_DIR/.venv/bin/python3" -m uvicorn app.main:app --host 127.0.0.1 --port $PORT
