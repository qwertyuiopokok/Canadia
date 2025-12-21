#!/bin/bash

# Canadia Setup Script
# This script sets up the development environment for the Canadia project

set -e  # Exit on error

echo "🚀 Canadia Setup Script"
echo "======================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check Python version
echo "1️⃣  Vérification de Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé!"
    echo "   Veuillez installer Python 3.9 ou supérieur."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "   ✅ Python $PYTHON_VERSION trouvé"
echo ""

# Create virtual environment
if [ -d ".venv" ]; then
    echo "2️⃣  Virtual environment existe déjà"
    read -p "   Voulez-vous le recréer? (y/N) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "   🗑️  Suppression de l'ancien .venv..."
        rm -rf .venv
        echo "   📦 Création d'un nouveau virtual environment..."
        python3 -m venv .venv
    fi
else
    echo "2️⃣  Création du virtual environment..."
    python3 -m venv .venv
    echo "   ✅ Virtual environment créé"
fi
echo ""

# Activate virtual environment
echo "3️⃣  Activation du virtual environment..."
source .venv/bin/activate
echo "   ✅ Virtual environment activé"
echo ""

# Upgrade pip
echo "4️⃣  Mise à jour de pip..."
pip install --upgrade pip -q
echo "   ✅ pip mis à jour"
echo ""

# Install dependencies
echo "5️⃣  Installation des dépendances..."
if [ -f "requirements.txt" ]; then
    echo "   📚 Installation depuis requirements.txt..."
    pip install -r requirements.txt
    echo "   ✅ Dépendances installées"
else
    echo "   ⚠️  requirements.txt non trouvé!"
    echo "   Installation des dépendances de base..."
    pip install fastapi uvicorn[standard] python-dotenv
    echo "   ✅ Dépendances de base installées"
fi
echo ""

# Check if backend directory exists
if [ ! -d "backend/app" ]; then
    echo "⚠️  Le dossier backend/app n'existe pas!"
    echo "   Assurez-vous d'être dans le bon répertoire."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "6️⃣  Création du fichier .env..."
    cat > .env << EOF
# Canadia Environment Variables
# Add your configuration here
EOF
    echo "   ✅ Fichier .env créé"
else
    echo "6️⃣  Fichier .env existe déjà"
fi
echo ""

echo "✅ Configuration terminée!"
echo ""
echo "Pour démarrer le serveur:"
echo "  ./start_canadia.sh"
echo ""
echo "Ou manuellement:"
echo "  source .venv/bin/activate"
echo "  cd backend"
echo "  uvicorn app.main:app --reload --host 0.0.0.0 --port 9800"
echo ""
echo "Le serveur sera accessible sur:"
echo "  - http://localhost:9800"
echo "  - http://localhost:9800/docs (documentation API)"
echo ""
