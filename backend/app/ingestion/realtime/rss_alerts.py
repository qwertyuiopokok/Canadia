# Gestion des flux RSS d’urgence pour ingestion temps réel

import feedparser
from datetime import datetime

def fetch_alerts_rss(url: str) -> list:
	feed = feedparser.parse(url)
	alerts = []

	for entry in feed.entries:
		alerts.append({
			"title": entry.get("title", ""),
			"content": entry.get("summary", ""),
			"url": entry.get("link"),
			"published": entry.get("published", None),
			"fetched_at": datetime.utcnow().isoformat()
		})

	return alerts
