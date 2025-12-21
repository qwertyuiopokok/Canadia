from datetime import datetime

from fastapi import APIRouter

router = APIRouter(tags=["status"])


@router.get("/status")
def status():
	return {"status": "OK", "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


@router.get("/health")
def health():
	return {"status": "ok"}
