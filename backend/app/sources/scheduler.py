"""
Automation for periodic ingestion (cron, APScheduler, etc.)
"""
from apscheduler.schedulers.background import BackgroundScheduler
import time

def schedule_ingestion(ingest_func, interval_minutes=60):
	"""
	Schedule the given ingest_func to run every interval_minutes.
	"""
	scheduler = BackgroundScheduler()
	scheduler.add_job(ingest_func, 'interval', minutes=interval_minutes)
	scheduler.start()
	print(f"Ingestion scheduled every {interval_minutes} minutes. Press Ctrl+C to exit.")
	try:
		while True:
			time.sleep(60)
	except (KeyboardInterrupt, SystemExit):
		scheduler.shutdown()
