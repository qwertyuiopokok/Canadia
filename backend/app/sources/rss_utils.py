import feedparser
from typing import List, Dict
from datetime import datetime

def fetch_rss_from_urls(urls: List[str], source_id: str = None) -> List[Dict]:
    articles = []
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title", ""),
                "content": entry.get("summary", entry.get("description", "")),
                "url": entry.get("link"),
                "published": entry.get("published", None),
                "fetched_at": datetime.utcnow().isoformat(),
                "source_id": source_id,
                "rss_url": url
            })
    return articles
