import pika
import json
import requests
from backend.app.api.document_to_signal import document_to_signal
from datetime import datetime

RABBITMQ_URL = "amqp://guest:guest@localhost:5672/"
QUEUE_NAME = "news_queue"
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

def consume_and_save_rabbitmq():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    print("Attente de nouveaux articles dans RabbitMQ...")
    def callback(ch, method, properties, body):
        article = json.loads(body.decode())
        doc = rss_to_document(article)
        signal = document_to_signal(doc)
        try:
            resp = requests.post(API_URL, json=signal, timeout=5)
            print(f"Signal enregistré (status {resp.status_code}):", resp.json())
        except Exception as e:
            print("Erreur d'enregistrement:", e)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    channel.start_consuming()

if __name__ == "__main__":
    consume_and_save_rabbitmq()
