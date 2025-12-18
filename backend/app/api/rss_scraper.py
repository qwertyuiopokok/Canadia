import feedparser
from typing import List, Dict

# Exemple de flux RSS d’actualité (Radio-Canada, Le Devoir, CBC)
RSS_FEEDS = [
    "https://ici.radio-canada.ca/rss/4159",
    "https://www.ledevoir.com/rss/actualites.xml",
    "https://www.cbc.ca/cmlink/rss-topstories"
]

def fetch_rss_articles() -> List[Dict]:
    """Récupère les articles récents de plusieurs flux RSS."""
    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title"),
                "link": entry.get("link"),
                "summary": entry.get("summary"),
                "published": entry.get("published"),
                "source": url
            })
    return articles

if __name__ == "__main__":
    for art in fetch_rss_articles():
        print(art)
