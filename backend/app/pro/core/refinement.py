def refine_answer(initial_answer: str, new_answers: dict) -> str:
    """
    Améliore la réponse initiale en intégrant les nouvelles réponses utilisateur.
    """
    # Placeholder: implement LLM or rule-based refinement
    return initial_answer + " (réponse affinée)"

def provisional_answer(base_answer: str, missing: list) -> str:
    if not missing:
        return base_answer

    return (
        base_answer
        + "\n\n⚠️ Cette réponse est provisoire. "
        + "Elle pourra être précisée avec les informations suivantes."
    )
