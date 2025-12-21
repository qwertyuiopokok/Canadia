from fastapi import APIRouter

router = APIRouter(tags=["ask_anything"])


@router.get("/ask_anything")
def ask_anything_placeholder():
    return {"error": "Not implemented", "status": 501}
from fastapi import APIRouter

router = APIRouter(tags=["ask_anything"])


@router.get("/ask_anything")
def ask_anything_placeholder():
	return {"error": "Not implemented", "status": 501}
