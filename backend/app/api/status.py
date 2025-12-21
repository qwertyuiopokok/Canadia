from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/status")
def get_status():
    """Return the platform status"""
    return {
        "status": "ok",
        "date": datetime.now().isoformat()
    }
