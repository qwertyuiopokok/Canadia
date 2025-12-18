import redis
import json
from .rss_scraper import fetch_rss_articles

REDIS_STREAM = "news_stream"
REDIS_URL = "redis://localhost:6379/0"


def push_articles_to_redis():
    r = redis.Redis.from_url(REDIS_URL)
    articles = fetch_rss_articles()
    for art in articles:
        r.xadd(REDIS_STREAM, {"data": json.dumps(art)})
    print(f"{len(articles)} articles envoyés dans le stream Redis '{REDIS_STREAM}'")

if __name__ == "__main__":
    push_articles_to_redis()
