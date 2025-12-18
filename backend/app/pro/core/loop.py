from .clarity import detect_clarity_issues
from .counter_questions import generate_counter_questions
from .refinement import refine_answer

def diagnostic_cycle(question: str, answer: str, user_new_answers: dict = None) -> dict:
    """
    Orchestration du cycle diagnostic :
    1. Analyse de clarté
    2. Génération de contre-questions
    3. Réponse affinée
    """
    clarity = detect_clarity_issues(question, answer)
    counter_questions = generate_counter_questions(clarity["uncertainties"])
    refined = refine_answer(answer, user_new_answers or {})
    return {
        "clarity": clarity,
        "counter_questions": counter_questions,
        "refined_answer": refined
    }
