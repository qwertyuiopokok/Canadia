import requests
import redis
import json
from backend.app.api.document_to_signal import document_to_signal
from datetime import datetime

REDIS_STREAM = "news_stream"
REDIS_URL = "redis://localhost:6379/0"
API_URL = "http://localhost:8000/signals"

def rss_to_document(article):
    return {
        "id": article.get("link", "") + "-" + datetime.now().isoformat(),
        "titre": article.get("title", ""),
        "resume": article.get("summary", ""),
        "contenu": article.get("summary", ""),
        "source": {
            "nom": article.get("source", "RSS"),
            "url": article.get("link", ""),
            "type": "media"
        },
        "geographie": {"niveau": "canada"},
        "themes": ["actualité"],
        "date_publication": article.get("published", "")
    }

def consume_and_save_redis():
    r = redis.Redis.from_url(REDIS_URL)
    last_id = '0-0'
    print("Attente de nouveaux articles dans Redis Stream...")
    while True:
        messages = r.xread({REDIS_STREAM: last_id}, block=0, count=10)
        for stream, entries in messages:
            for entry_id, data in entries:
                article = json.loads(data[b'data'].decode())
                doc = rss_to_document(article)
                signal = document_to_signal(doc)
                try:
                    resp = requests.post(API_URL, json=signal, timeout=5)
                    print(f"Signal enregistré (status {resp.status_code}):", resp.json())
                except Exception as e:
                    print("Erreur d'enregistrement:", e)
                last_id = entry_id.decode()

if __name__ == "__main__":
    consume_and_save_redis()
