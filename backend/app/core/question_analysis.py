def analyse_question(question: str) -> dict:
    q = question.lower()
    themes = []
    if "logement" in q or "loyer" in q:
        themes.append("logement")
    if "santé" in q or "maladie" in q:
        themes.append("santé")
    if "éducation" in q or "école" in q:
        themes.append("éducation")
    if "québec" in q:
        geo = "QC"
    else:
        geo = "CANADA"

    # Détection du type de question
    if any(word in q for word in ["comment", "procédure", "démarche", "obtenir", "faire pour"]):
        question_type = "procédure"
    elif any(word in q for word in ["contact", "joindre", "téléphone", "adresse"]):
        question_type = "contact"
    elif any(word in q for word in ["aide", "soutien", "assistance"]):
        question_type = "aide"
    else:
        question_type = "information"

    return {
        "themes": themes,
        "geo": geo,
        "type": question_type,
        "raw": question
    }


def generate_internal_summaries(contents: list):
    """
    Génère un résumé, une FAQ et des points clés à partir d'une liste de contenus.
    (Ici, version placeholder à remplacer par une vraie implémentation LLM ou heuristique.)
    """
    return {
        "summary": "...",
        "faq": [],
        "key_points": []
    }
