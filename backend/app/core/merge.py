"""
Fusionne les résultats internes et externes en une seule liste homogène.
"""

def merge(internal: list, external: list) -> list:
    """
    Fusionne les contenus internes (format natif) et externes (déjà formatés).
    Args:
        internal (list): Résultats internes (dicts avec 'content' et 'source').
        external (list): Résultats externes (déjà formatés).
    Returns:
        list: Liste fusionnée, formatée pour la réponse finale.
    """
    merged = []

    for c in internal:
        merged.append({
            "text": c["content"],
            "source": c["source"]["name"],
            "confidence": "high"
        })

    for c in external:
        merged.append(c)

    return merged
