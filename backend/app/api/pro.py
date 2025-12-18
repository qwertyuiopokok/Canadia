from fastapi import APIRouter, Depends
from app.pro.engine import ask_pro
from app.auth.dependencies import require_pro_subscription

router = APIRouter(prefix="/pro", tags=["Canadia Pro"])

@router.post("/ask")
def ask_pro_endpoint(
    payload: dict,
    company=Depends(require_pro_subscription)
):
    return ask_pro(
        question=payload["question"],
        company_context=company
    )
