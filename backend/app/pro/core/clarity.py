def update_context(context: dict, user_answers: dict) -> dict:
    for k, v in user_answers.items():
        if v:
            context[k] = v
    return context
def detect_clarity_issues(question: str, answer: str) -> dict:
    """
    Détecte le flou ou le manque de clarté dans la réponse à une question.
    Retourne un dict avec les zones d'incertitude ou de manque.
    """
    # Placeholder: implement LLM or rule-based detection
    return {"uncertainties": [], "is_clear": True}

def analyze_clarity(question: str, context: dict) -> dict:
    missing = []

    if not context.get("company_size"):
        missing.append("taille_entreprise")

    if not context.get("project_type"):
        missing.append("type_projet")

    if not context.get("constraints"):
        missing.append("contraintes")

    is_clear = len(missing) == 0

    return {
        "is_clear": is_clear,
        "missing": missing
    }
