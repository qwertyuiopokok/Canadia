def detect_anomaly(theme: str, stats: dict) -> bool:
    """
    Détecte un thème qui explose
    sans couverture suffisante.
    """
    total = stats["count"]
    full = stats["full"]

    if total < 5:
        return False  # trop tôt

    coverage_ratio = full / total if total else 0

    # règle simple mais efficace
    if total >= 10 and coverage_ratio < 0.4:
        return True

    return False
