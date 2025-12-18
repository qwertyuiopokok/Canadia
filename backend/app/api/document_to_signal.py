from typing import Dict, Any, Optional
from uuid import UUID, uuid4
from datetime import date

def document_to_signal(document: Dict[str, Any], valeur: float = 1.0, audience: Optional[str] = None) -> Dict[str, Any]:
    """
    Convertit un document (dict) au format Signal (dict) pour l'API.
    - valeur: float, valeur du signal (défaut 1.0)
    - audience: str, cible du signal (optionnel)
    """
    return {
        "content_id": document.get("id", str(uuid4())),
        "valeur": valeur,
        "date": document.get("date_publication", date.today().isoformat()),
        "contexte": document.get("titre"),
        "audience": audience or "",
        "geographie": {
            "niveau": document.get("geographie", {}).get("niveau", "canada"),
            "description": "Automatique depuis Document"
        },
        "source": document.get("source", {})
    }

# Exemple d'utilisation :
if __name__ == "__main__":
    doc = {
        "id": "log-can-002",
        "titre": "Principaux programmes fédéraux en logement",
        "date_publication": "2024-01-01",
        "geographie": {"niveau": "canada"},
        "source": {"nom": "Société canadienne d’hypothèques et de logement", "url": "https://www.cmhc-schl.gc.ca", "type": "organisme"}
    }
    signal = document_to_signal(doc, audience="Ménages, provinces, municipalités")
    print(signal)
