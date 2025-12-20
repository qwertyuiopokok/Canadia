from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def get_status():
    """Health check endpoint"""
    return {"status": "ok"}
