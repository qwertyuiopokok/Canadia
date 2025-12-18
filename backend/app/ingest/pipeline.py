"""
General ingestion pipeline for multiple content types (RSS, API, web, video).
Each fetcher returns a list of normalized dicts with at least:
- title
- link/url
- summary/description
- published/date
- source/type
"""

from typing import List, Dict
from backend.app.api import rss_scraper
from backend.app.ingest import fetch_google
# Future: from . import fetch_youtube, fetch_govapi, fetch_community

GOOGLE_QUERIES = [
    "gouvernement logement Québec",
    "aide sociale Québec",
    "santé publique Canada"
]

def ingest_all() -> List[Dict]:
    all_content = []
    # Media (RSS)
    all_content.extend(rss_scraper.fetch_rss_articles())
    # Google Search
    for query in GOOGLE_QUERIES:
        all_content.extend(fetch_google.fetch_google_search(query))
    # TODO: Add government, community, video fetchers here
    # all_content.extend(fetch_govapi.fetch_articles())
    # all_content.extend(fetch_community.fetch_news())
    # all_content.extend(fetch_youtube.fetch_videos())
    return all_content

if __name__ == "__main__":
    for item in ingest_all():
        print(item)
