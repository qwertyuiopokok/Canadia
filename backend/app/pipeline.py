
from app.sources.registry import SOURCES
from app.sources.rss import fetch_rss
from app.processing.normalize import normalize
from app.processing.tagger import tag_content
from app.processing.deduplicate_and_update import deduplicate_and_update


def run_ingestion():
    results = []
    raw_items = fetch_rss()
    for raw in raw_items:
        # Find the source for this article
        source = next((s for s in SOURCES if s["id"] == raw.get("source_id")), None)
        if source is None:
            continue
        normalized = normalize(raw, source)
        tagged = tag_content(normalized)
        final = deduplicate_and_update(tagged)
        results.append(final)
    return results

if __name__ == "__main__":
    for item in run_ingestion():
        print(item)
