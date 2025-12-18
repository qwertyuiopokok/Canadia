"""
Calcule le score de confiance global à partir des contenus fusionnés.
"""

def compute_confidence(contents: list) -> str:
    """
    Calcule le score de confiance global à partir des contenus.
    Args:
        contents (list): Liste de dicts avec une clé 'confidence'.
    Returns:
        str: "faible", "moyenne" ou "élevée".
    """
    if not contents:
        return "faible"
    if any(c["confidence"] == "high" for c in contents):
        return "élevée"
    return "moyenne"
