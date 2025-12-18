from app.pro.core.clarity import analyze_clarity
from app.pro.core.counter_questions import generate_counter_questions
from app.pro.core.refinement import provisional_answer
from app.pro.intelligence.similarity_engine.compare import find_similar_cases
from app.pro.intelligence.synthesis.explain import synthesize_answer

MAX_CYCLES = 3

def precision_loop(question: str, context: dict, cycle: int = 1):
    """
    Boucle centrale de réponse intelligente.
    """
    # 1. Analyse de clarté
    clarity = analyze_clarity(question, context)

    # 2. Recherche de cas similaires
    similar_cases = find_similar_cases(context)

    # 3. Synthèse basée sur trajectoires réelles
    base_answer = synthesize_answer(
        question=question,
        context=context,
        similar_cases=similar_cases
    )

    # 4. Réponse provisoire si nécessaire
    final_answer = provisional_answer(
        base_answer,
        clarity["missing"]
    )

    # 5. Génération de contre-questions
    counter_questions = []
    if not clarity["is_clear"] and cycle < MAX_CYCLES:
        counter_questions = generate_counter_questions(
            clarity["missing"]
        )

    return {
        "answer": final_answer,
        "cycle": cycle,
        "needs_refinement": len(counter_questions) > 0,
        "counter_questions": counter_questions,
        "similar_cases_used": len(similar_cases)
    }
