from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/ask_anything")
def ask_anything(question: str = Query(..., description="Question à poser")):
    """General question endpoint"""
    return JSONResponse({
        "answer": "Cette fonctionnalité est en développement.",
        "question": question
    })
