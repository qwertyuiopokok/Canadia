from app.pro.core.questions_by_capability import QUESTIONS_BY_CAPABILITY

def build_questionnaire(context: dict) -> list:
    """
    Construit un questionnaire adapté
    au métier et au secteur.
    """
    questions = []
    seen = set()

    for cap in context.get("capabilities", []):
        for q in QUESTIONS_BY_CAPABILITY.get(cap, []):
            if q not in seen:
                questions.append({
                    "capability": cap,
                    "question": q
                })
                seen.add(q)

    return questions
