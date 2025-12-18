from app.ingestion.cleaner import clean_text

def normalize_alert(raw: dict, source: dict) -> dict:
	return {
		"title": clean_text(raw.get("title")),
		"content": clean_text(raw.get("content")),
		"url": raw.get("url"),
		"source": {
			"id": source["id"],
			"name": source["name"],
			"type": source["type"]
		},
		"published": raw.get("published"),
		"content_type": "alert",   # 🔥 DIFFÉRENT DE news
		"priority": "high",
		"status": "new"
	}
"""
Content normalization utilities
"""
def normalize(raw: dict, source: dict) -> dict:
	return {
		"title": raw.get("title"),
		"content": raw.get("content"),
		"url": raw.get("url"),
		"source": {
			"id": source["id"],
			"name": source["name"],
			"type": source["type"]
		},
		"published": raw.get("published"),
		"content_type": "news",  # 👈 IMPORTANT
		"status": "new"
	}
