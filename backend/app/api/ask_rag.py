from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AskRagRequest(BaseModel):
    question: str

@router.post("/ask-rag")
def ask_rag(req: AskRagRequest):
    """Ask with RAG (Retrieval-Augmented Generation) endpoint"""
    return {"answer": f"Question RAG reçue: {req.question}"}
