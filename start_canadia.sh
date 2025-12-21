#!/bin/bash

PORT=9800

echo "🔎 Nettoyage du port $PORT..."
lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null

echo "🚀 Lancement de Canadia sur le port $PORT..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate virtual environment from the script directory
source "$SCRIPT_DIR/.venv/bin/activate"

# Change to backend directory and run uvicorn
cd "$SCRIPT_DIR/backend"
python3 -m uvicorn app.main:app --host 127.0.0.1 --port $PORT
