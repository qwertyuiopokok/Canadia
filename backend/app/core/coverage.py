
"""
Évaluation de la suffisance des contenus récupérés.
"""

def evaluate(contents: list) -> str:
    """
    Évalue la suffisance des contenus récupérés.
    Args:
        contents (list): Liste des contenus récupérés.
    Returns:
        str: "none", "partial" ou "full" selon la quantité.
    """
    if not contents:
        return "none"
    if len(contents) < 2:
        return "partial"
    return "full"
