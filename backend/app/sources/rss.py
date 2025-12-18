"""
RSS source fetcher (media, government, etc.)
"""
from .registry import SOURCES
from .rss_utils import fetch_rss_from_urls

def fetch_rss() -> list:
	all_articles = []
	for src in SOURCES:
		rss_urls = src.get("rss", [])
		if rss_urls:
			articles = fetch_rss_from_urls(rss_urls, source_id=src["id"])
			for art in articles:
				art["source_name"] = src["name"]
				art["source_type"] = src["type"].value if hasattr(src["type"], "value") else str(src["type"])
				art["priority"] = src["priority"]
				art["trust"] = src["trust"]
			all_articles.extend(articles)
	return all_articles
