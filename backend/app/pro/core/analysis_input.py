# Structure d'entrée pour l'analyse

def build_analysis_input(context: dict, questionnaire_answers: dict, user_question: str) -> dict:
    return {
        "context": context,
        "answers": questionnaire_answers,
        "question": user_question
    }
