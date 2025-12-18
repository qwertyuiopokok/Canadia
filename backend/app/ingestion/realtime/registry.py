# Sources d’alertes pour ingestion temps réel

ALERT_SOURCES = [
	{
		"id": "canada-alerts",
		"name": "Gouvernement du Canada — Alertes",
		"type": "government",
		"priority": 1,
		"trust": 1.0,
		"rss": [
			"https://www.canada.ca/en/news/web-feeds/rss/alerts.xml"
		]
	},
	{
		"id": "qc-urgences",
		"name": "Québec — Urgences",
		"type": "government",
		"priority": 1,
		"trust": 1.0,
		"rss": [
			"https://www.quebec.ca/rss/urgences.xml"
		]
	}
]
