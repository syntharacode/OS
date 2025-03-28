from fastapi import APIRouter, Query
from backend.utils.logger_store import get_logs

# Initialize a FastAPI router for system-related endpoints
router = APIRouter()

# GET endpoint to fetch system logs
@router.get("/api/system/logs")
async def fetch_logs(limit: int = Query(50, ge=1, le=1000), level: str = Query(None)):
    """
    Fetch system logs with optional pagination and log level filtering.

    Query Parameters:
    - limit: Maximum number of log entries to return (default: 50, min: 1, max: 1000)
    - level: Optional log level filter (e.g., INFO, ERROR, WARNING)

    Returns:
    - A JSON response containing the filtered and paginated logs.
    """
    return {"logs": get_logs(limit=limit, level=level)}
