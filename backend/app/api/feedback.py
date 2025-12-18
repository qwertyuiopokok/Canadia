from fastapi import APIRouter
from pydantic import BaseModel
from app.storage.feedback_store import save_feedback

router = APIRouter(
    prefix="/feedback",
    tags=["feedback"]
)

class FeedbackRequest(BaseModel):
    fingerprint: str
    value: int  # 1 = like, -1 = dislike

@router.post("/")
def submit_feedback(payload: FeedbackRequest):
    if payload.value not in (1, -1):
        return {"status": "error", "message": "Invalid value"}

    save_feedback(payload.fingerprint, payload.value)
    return {"status": "ok"}
