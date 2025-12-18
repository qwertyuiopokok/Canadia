import time
from app.core.cache import get_cache, set_cache
from app.core.fallback import fallback_answer

def canadia_kernel(question: str, context: dict, engine_fn):
    """
    Cerveau central Canadia
    """
    start = time.time()
    cache_key = f"{engine_fn.__name__}:{question}"

    # 1. Cache (ultra rapide)
    cached = get_cache(cache_key)
    if cached:
        cached["meta"] = {"cached": True}
        return cached

    # 2. Validation minimale
    if not question or len(question.strip()) < 5:
        return fallback_answer(
            "Pouvez-vous préciser davantage votre question ?"
        )

    try:
        # 3. Appel du moteur spécialisé
        response = engine_fn(question, context)

    except Exception:
        response = fallback_answer(
            "Une réponse complète n’est pas disponible pour le moment."
        )

    # 4. Ajout métadonnées
    response["meta"] = {
        "cached": False,
        "duration_ms": int((time.time() - start) * 1000)
    }

    # 5. Mise en cache
    set_cache(cache_key, response)

    return response
