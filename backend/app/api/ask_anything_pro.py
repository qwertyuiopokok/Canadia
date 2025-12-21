from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/ask_anything_pro")
def ask_anything_pro(question: str = Query(..., description="Question à poser")):
    """Pro question endpoint"""
    return JSONResponse({
        "answer": "Cette fonctionnalité Pro est en développement.",
        "question": question
    })
