#!/bin/bash

PORT=9800

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if virtual environment exists
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
    echo "❌ Virtual environment not found!"
    echo ""
    echo "Please create and setup the virtual environment first:"
    echo "  1. python3 -m venv .venv"
    echo "  2. source .venv/bin/activate"
    echo "  3. pip install --upgrade pip"
    echo "  4. pip install -r requirements.txt"
    echo ""
    echo "Or run: bash setup.sh (if available)"
    exit 1
fi

# Check if requirements are installed
if ! "$SCRIPT_DIR/.venv/bin/python" -c "import fastapi" 2>/dev/null; then
    echo "⚠️  Dependencies not installed!"
    echo ""
    echo "Please install dependencies:"
    echo "  source .venv/bin/activate"
    echo "  pip install -r requirements.txt"
    echo ""
    exit 1
fi

echo "🔎 Nettoyage du port $PORT..."
lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null

echo "🚀 Lancement de Canadia sur le port $PORT..."

# Activate virtual environment from the script directory
source "$SCRIPT_DIR/.venv/bin/activate"

# Change to backend directory and run uvicorn
cd "$SCRIPT_DIR/backend"
echo "📡 Serveur accessible sur:"
echo "   - Local:  http://localhost:$PORT"
echo "   - Réseau: http://$(hostname -I | awk '{print $1}'):$PORT (si configuré)"
echo "   - Docs:   http://localhost:$PORT/docs"
echo ""
python3 -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
