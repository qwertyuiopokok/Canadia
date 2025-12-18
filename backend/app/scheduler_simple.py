import time
from app.pipeline import run_ingestion

def start_scheduler(interval_minutes=30):
    while True:
        run_ingestion()
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    start_scheduler()
