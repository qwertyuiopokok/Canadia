#!/bin/bash

PORT=9800

echo "🔎 Nettoyage du port $PORT..."
lsof -ti tcp:$PORT | xargs kill -9 2>/dev/null

echo "🚀 Lancement de Canadia sur le port $PORT..."
cd backend
source ../.venv/bin/activate
python3 -m uvicorn app.main:app --host 127.0.0.1 --port $PORT
