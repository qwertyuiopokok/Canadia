from fastapi import APIRouter
from app.pro.core.build_questionnaire import build_questionnaire
from app.pro.registry.context import build_context

router = APIRouter()

@router.post("/sector/questionnaire")
def get_questionnaire(payload: dict):
    context = build_context(payload)
    questions = build_questionnaire(context)

    return {
        "sector": context.get("sector"),
        "job": context.get("job"),
        "questions": questions
    }
