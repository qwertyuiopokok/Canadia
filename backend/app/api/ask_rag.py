from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/ask_rag")
def ask_rag(question: str = Query(..., description="Question à poser")):
    """RAG-based question endpoint"""
    return JSONResponse({
        "answer": "Cette fonctionnalité RAG est en développement.",
        "question": question
    })
