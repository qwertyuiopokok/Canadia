# Canadia 🇨🇦

Plateforme de recherche citoyenne canadienne - Un moteur de recherche citoyen pour tous.

## Description

Canadia est une plateforme FastAPI qui fournit un moteur de recherche et des services d'information pour les citoyens canadiens. Elle combine des recherches web, des flux RSS, et un système de récupération augmentée par génération (RAG) pour fournir des réponses pertinentes aux questions des utilisateurs.

## Démarrage Rapide

### Prérequis

- Python 3.9+
- pip (gestionnaire de paquets Python)

### Installation et Démarrage

1. **Lancer Canadia avec le script de démarrage:**

```bash
./start_canadia.sh
```

Le serveur démarrera automatiquement sur le port `9800`

2. **Accéder à l'interface web:**

- **En local:** `http://localhost:9800`
- **Via GitHub Codespaces:** Le port sera automatiquement forwarded. Utilisez l'URL fournie par Codespaces (ex: `https://[votre-codespace]-9800.app.github.dev`)
- **Interface de test:** Ouvrez `index.html` dans votre navigateur pour une interface alternative

### Installation Manuelle

Si vous préférez installer et démarrer manuellement:

```bash
# Naviguer vers le répertoire backend
cd backend

# Activer l'environnement virtuel
source .venv/bin/activate

# Installer les dépendances (première fois seulement)
pip install -r requirements.txt

# Démarrer le serveur (accessible de partout)
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 9800
```

## Fonctionnalités

- **Recherche Web**: Recherche d'informations sur le web via l'API
- **Flux RSS**: Agrégation de nouvelles et actualités
- **Suggestions**: Suggestions automatiques basées sur l'actualité
- **API REST**: Points d'accès API complets pour l'intégration
- **Interface Web**: Interface utilisateur moderne et responsive

## Points d'Accès API Principaux

- `GET /` - Page d'accueil avec moteur de recherche
- `GET /status` - État du serveur
- `GET /ask` - Poser une question
- `GET /suggestions` - Obtenir des suggestions d'actualités
- `GET /docs` - Documentation API interactive (Swagger)

## Structure du Projet

```
Canadia/
├── backend/
│   ├── app/
│   │   ├── api/          # Points d'accès API
│   │   ├── core/         # Logique métier
│   │   ├── storage/      # Gestion des données
│   │   ├── templates/    # Templates HTML
│   │   └── main.py       # Application FastAPI principale
│   ├── requirements.txt   # Dépendances Python
│   └── .venv/            # Environnement virtuel
├── start_canadia.sh      # Script de démarrage
└── index.html            # Interface web alternative
```

## Configuration

L'application utilise un fichier `.env` pour la configuration. Les variables d'environnement principales incluent:

- `XAI_API_KEY` - Clé API pour les services d'IA (optionnel)

## Développement

Pour le développement avec rechargement automatique:

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 9800
```

## Dépannage

### Le serveur ne démarre pas

- Vérifiez que le port 9800 n'est pas déjà utilisé
- Assurez-vous que toutes les dépendances sont installées: `pip install -r backend/requirements.txt`

### Erreur de module manquant

Réinstallez les dépendances:
```bash
cd backend
source .venv/bin/activate
pip install -r requirements.txt
```

## Support

Pour les problèmes ou questions, veuillez ouvrir une issue sur GitHub.

## Licence

© 2025 Canadia. Rouge, blanc et bleu pour tous.
