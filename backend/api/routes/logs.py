from fastapi import APIRouter
from backend.utils.logger_store import get_logs

router = APIRouter()

@router.get("/api/system/logs")
async def fetch_logs():
    return {"logs": get_logs()}