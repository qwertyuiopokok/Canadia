"""
Génération de questions internes pour auto-questionnement thématique.
"""

THEMES = ["logement", "santé", "éducation", "emploi"]
PROVINCES = ["QC", "ON", "BC"]

def generate_self_questions():
    questions = []
    for theme in THEMES:
        for province in PROVINCES:
            questions.append(
                f"Quelles informations officielles récentes concernent {theme} au {province} ?"
            )
    return questions
