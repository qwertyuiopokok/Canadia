COUNTER_QUESTION_MAP = {
    "taille_entreprise": "Quelle est la taille approximative de votre entreprise ou équipe ?",
    "type_projet": "De quel type de projet s’agit-il exactement ?",
    "contraintes": "Quelles sont vos principales contraintes (temps, ressources, sécurité, etc.) ?"
}

def generate_counter_questions(missing: list) -> list:
    return [
        COUNTER_QUESTION_MAP[m]
        for m in missing
        if m in COUNTER_QUESTION_MAP
    ]
