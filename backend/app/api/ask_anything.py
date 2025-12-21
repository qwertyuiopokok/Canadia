from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AskAnythingRequest(BaseModel):
    question: str

@router.post("/ask-anything")
def ask_anything(req: AskAnythingRequest):
    """Ask anything endpoint"""
    return {"answer": f"Question reçue: {req.question}"}
