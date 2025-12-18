from fastapi import APIRouter
from backend.app.main import FilterPayload

router = APIRouter(prefix="/filters", tags=["Filters"])

@router.post("")
def apply_filters(payload: FilterPayload):
    return payload
