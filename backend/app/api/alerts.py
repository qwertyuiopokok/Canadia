
from fastapi import APIRouter
from app.storage.content_store import all_contents
from app.ingestion.realtime.pipeline import run_realtime_ingestion

router = APIRouter()

@router.get("/alerts")
def get_alerts():
    contents = all_contents()
    return [
        c for c in contents
        if c.get("content_type") == "alert"
    ]

@router.post("/admin/ingest/alerts")
def ingest_alerts():
    results = run_realtime_ingestion()
    return {
        "status": "ok",
        "alerts_processed": len(results)
    }
