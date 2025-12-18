"""
Analyse de la question pour déterminer le domaine principal.
"""

def analyze(question: str) -> dict:
    """
    Analyse une question pour en extraire le domaine principal.
    Args:
        question (str): La question utilisateur.
    Returns:
        dict: Dictionnaire avec la question et le domaine détecté.
    """
    q = question.lower()

    domain = "general"
    if any(w in q for w in ["logement", "loyer", "habitation"]):
        domain = "logement"
    elif any(w in q for w in ["santé", "hôpital"]):
        domain = "sante"
    elif any(w in q for w in ["urgence", "alerte"]):
        domain = "alerte"

    return {
        "question": question,
        "domain": domain
    }
