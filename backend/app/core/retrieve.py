"""
Récupération des contenus internes selon le domaine.
"""
from app.storage.content_store import all_contents

def retrieve_internal(domain: str) -> list:
    """
    Récupère les contenus dont le thème correspond au domaine donné.
    Args:
        domain (str): Domaine à filtrer (ou 'general' pour tout).
    Returns:
        list: Liste des contenus filtrés.
    """
    results = []
    for c in all_contents():
        if domain in c.get("themes", []) or domain == "general":
            results.append(c)
    return results
