def compute_priority(content: dict) -> int:
    if content.get("content_type") == "alert":
        return 100  # toujours au-dessus

    if content.get("content_type") == "news":
        return 10

    return 1
from datetime import datetime

def quality_score(content: dict) -> float:
    score = 0.0

    # Source
    if content["source"]["type"] == "government":
        score += 3
    elif content["source"]["type"] == "media":
        score += 2

    # Fraîcheur
    if content.get("last_updated"):
        age = (
            datetime.utcnow()
            - datetime.fromisoformat(content["last_updated"])
        ).total_seconds() / 3600
        if age < 24:
            score += 2
        elif age < 72:
            score += 1

    # Feedback
    score += content.get("feedback_score", 0) * 0.5

    return score
