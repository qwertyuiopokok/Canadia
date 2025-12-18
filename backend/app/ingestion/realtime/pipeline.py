# Pipeline d’ingestion temps réel pour alertes

from app.ingestion.realtime.registry import ALERT_SOURCES
from app.ingestion.realtime.rss_alerts import fetch_alerts_rss
from app.processing.normalize import normalize_alert
from app.processing.tagger import tag_content
from app.processing.deduplicate_and_update import deduplicate_and_update

def run_realtime_ingestion():
	results = []

	for source in ALERT_SOURCES:
		for rss_url in source.get("rss", []):
			raw_items = fetch_alerts_rss(rss_url)

			for raw in raw_items:
				normalized = normalize_alert(raw, source)
				tagged = tag_content(normalized)
				final = deduplicate_and_update(tagged)
				results.append(final)

	return results
