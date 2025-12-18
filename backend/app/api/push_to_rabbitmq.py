import pika
import json
from .rss_scraper import fetch_rss_articles

RABBITMQ_URL = "amqp://guest:guest@localhost:5672/"
QUEUE_NAME = "news_queue"

def push_articles_to_rabbitmq():
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    articles = fetch_rss_articles()
    for art in articles:
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=json.dumps(art),
            properties=pika.BasicProperties(delivery_mode=2)
        )
    print(f"{len(articles)} articles envoyés dans la queue RabbitMQ '{QUEUE_NAME}'")
    connection.close()

if __name__ == "__main__":
    push_articles_to_rabbitmq()
