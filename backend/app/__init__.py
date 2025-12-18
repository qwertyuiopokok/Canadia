import threading
import time
from .learning.learning_loop import autonomous_learning_cycle


def nightly_learning():
    while True:
        autonomous_learning_cycle()
        time.sleep(12 * 3600)  # toutes les 12h


def start_learning_loop():
    thread = threading.Thread(target=nightly_learning, daemon=True)
    thread.start()


# Enregistrement FastAPI (si contexte FastAPI)
try:
    from fastapi import FastAPI
    app = FastAPI()
    app.add_event_handler("startup", start_learning_loop)
except ImportError:
    pass
