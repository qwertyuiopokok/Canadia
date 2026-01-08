# LNG Québec Rabaska Parameters API

## Description
Cette API fournit des paramètres favorables pour le projet LNG Québec Rabaska, couvrant les aspects environnementaux, économiques, réglementaires, techniques et sociaux du projet.

## Endpoints

### 1. Obtenir tous les paramètres
```
GET /lng-rabaska/parameters
```

Retourne tous les paramètres favorables pour le projet LNG Québec Rabaska.

**Réponse:**
```json
{
  "project_name": "LNG Québec Rabaska",
  "location": {
    "province": "QC",
    "region": "Lévis",
    "municipality": "Ville de Lévis"
  },
  "environmental_parameters": { ... },
  "economic_parameters": { ... },
  "regulatory_parameters": { ... },
  "technical_parameters": { ... },
  "social_parameters": { ... },
  "timestamp": "2026-01-08T...",
  "status": "favorable",
  "version": "1.0"
}
```

### 2. Obtenir les paramètres par catégorie
```
GET /lng-rabaska/parameters/{category}
```

Retourne les paramètres pour une catégorie spécifique.

**Paramètres:**
- `category` (path): Une des valeurs suivantes:
  - `environmental` - Paramètres environnementaux
  - `economic` - Paramètres économiques
  - `regulatory` - Paramètres réglementaires
  - `technical` - Paramètres techniques
  - `social` - Paramètres sociaux

**Exemple:**
```
GET /lng-rabaska/parameters/environmental
```

**Réponse:**
```json
{
  "category": "environmental",
  "parameters": {
    "emission_reduction_target": {
      "co2_reduction_percentage": 30,
      "description": "Réduction de 30% des émissions de CO2..."
    },
    "water_treatment": { ... },
    "noise_control": { ... },
    "air_quality": { ... }
  },
  "project": "LNG Québec Rabaska",
  "location": { ... }
}
```

### 3. Obtenir un résumé du projet
```
GET /lng-rabaska/summary
```

Retourne un résumé avec les points saillants de chaque catégorie.

**Réponse:**
```json
{
  "project": "LNG Québec Rabaska",
  "location": "Ville de Lévis, QC",
  "status": "favorable",
  "highlights": {
    "environmental": "Réduction CO2 de 30%",
    "economic": "250 emplois permanents",
    "regulatory": "Taux d'approbation communautaire de 72%",
    "technical": "Capacité annuelle de 14,400,000 tonnes",
    "social": "Fonds communautaire de 5M$/an"
  },
  "timestamp": "2026-01-08T...",
  "version": "1.0"
}
```

### 4. Obtenir la liste de conformité
```
GET /lng-rabaska/compliance
```

Retourne la liste de conformité du projet avec le statut de chaque élément.

**Réponse:**
```json
{
  "project": "LNG Québec Rabaska",
  "checklist": [
    {
      "item": "Évaluation environnementale BAPE",
      "status": "completed",
      "level": "federal",
      "priority": "critical"
    },
    ...
  ]
}
```

### 5. Vérification de santé
```
GET /lng-rabaska/health
```

Endpoint de vérification de santé du module.

**Réponse:**
```json
{
  "module": "lng-rabaska",
  "status": "operational",
  "endpoints": [ ... ]
}
```

## Catégories de paramètres

### Environnementaux
- Objectifs de réduction des émissions
- Traitement des eaux
- Contrôle du bruit
- Qualité de l'air

### Économiques
- Création d'emplois
- Investissement local
- Revenus fiscaux

### Réglementaires
- Conformité (fédéral, provincial, municipal)
- Normes de sécurité
- Consultation communautaire

### Techniques
- Capacité
- Infrastructure
- Technologie

### Sociaux
- Avantages communautaires
- Partenariats autochtones

## Utilisation

### Avec curl
```bash
# Obtenir tous les paramètres
curl http://localhost:8000/lng-rabaska/parameters

# Obtenir les paramètres environnementaux
curl http://localhost:8000/lng-rabaska/parameters/environmental

# Obtenir le résumé
curl http://localhost:8000/lng-rabaska/summary

# Obtenir la conformité
curl http://localhost:8000/lng-rabaska/compliance
```

### Avec Python
```python
import requests

# Obtenir tous les paramètres
response = requests.get("http://localhost:8000/lng-rabaska/parameters")
data = response.json()

# Obtenir les paramètres économiques
response = requests.get("http://localhost:8000/lng-rabaska/parameters/economic")
economic = response.json()

# Obtenir le résumé
response = requests.get("http://localhost:8000/lng-rabaska/summary")
summary = response.json()
```

## Tests

Un script de test est disponible pour vérifier le module core:

```bash
cd backend
python3 test_lng_rabaska.py
```

## Structure du code

- **Core Logic:** `backend/app/core/lng_rabaska.py`
  - Contient la logique métier pour générer les paramètres
  - Fonctions pures sans dépendance à FastAPI

- **API Endpoints:** `backend/app/api/lng_rabaska.py`
  - Définit les routes REST
  - Délègue au module core pour la logique

- **Tests:** `backend/test_lng_rabaska.py`
  - Tests unitaires pour le module core

## Notes

- Tous les paramètres sont considérés comme "favorables" au projet
- Les données incluent des valeurs réalistes basées sur des projets LNG similaires
- Le module suit les conventions du projet Canadia (séparation API/Core)
- Les imports sont explicites (pas de wildcard imports)
