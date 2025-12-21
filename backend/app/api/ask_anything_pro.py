from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AskAnythingProRequest(BaseModel):
    question: str

@router.post("/ask-anything-pro")
def ask_anything_pro(req: AskAnythingProRequest):
    """Ask anything pro endpoint"""
    return {"answer": f"Question professionnelle reçue: {req.question}"}
