
from datetime import datetime
from app.processing.deduplicate import compute_fingerprint
from app.storage.content_store import get_by_fingerprint, save, save_history

def deduplicate_and_update(content: dict) -> dict:
    fp = compute_fingerprint(
        title=content["title"],
        url=content["url"],
        source_id=content["source"]["id"]
    )

    existing = get_by_fingerprint(fp)

    if not existing:
        content["fingerprint"] = fp
        content["status"] = "new"
        content["last_updated"] = datetime.utcnow().isoformat()
        save(content)
        return content

    if content["content"] != existing["content"]:
        save_history(
            fp,
            existing["content"],
            datetime.utcnow().isoformat()
        )
        existing["content"] = content["content"]
        existing["status"] = "updated"
        existing["last_updated"] = datetime.utcnow().isoformat()
        save(existing)
        return existing

    existing["status"] = "unchanged"
    save(existing)
    return existing
