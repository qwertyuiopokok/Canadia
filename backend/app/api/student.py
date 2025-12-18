from fastapi import APIRouter
from app.student.engine import ask_student

router = APIRouter()

@router.post("/ask")
def ask(payload: dict):
    context = {
        "level": payload.get("level"),
        "field": payload.get("field")
    }
    return ask_student(payload["question"], context)
