def fallback_answer(message: str):
    return {
        "title": "Analyse Canadia",
        "summary": message,
        "key_points": [
            "La question nécessite plus de contexte",
            "Certaines données peuvent être manquantes"
        ],
        "limits": "Analyse partielle",
        "disclaimer": "Réponse générée sans analyse complète."
    }
