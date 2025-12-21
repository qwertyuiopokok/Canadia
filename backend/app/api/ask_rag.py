from fastapi import APIRouter

router = APIRouter(tags=["ask_rag"])


@router.get("/ask_rag")
def ask_rag_placeholder():
    return {"error": "Not implemented", "status": 501}
from fastapi import APIRouter

router = APIRouter(tags=["ask_rag"])


@router.get("/ask_rag")
def ask_rag_placeholder():
	return {"error": "Not implemented", "status": 501}
