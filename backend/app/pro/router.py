from fastapi import APIRouter
from app.pro.economic.router import router as economic_router

router = APIRouter(prefix="/pro")
router.include_router(economic_router)
