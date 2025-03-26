from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.user_service import create_user, get_user_by_name

router = APIRouter()

class CreateUserPayload(BaseModel):
    username: str

@router.post("/api/user/create")
async def create_user_endpoint(payload: CreateUserPayload):
    if get_user_by_name(payload.username):
        raise HTTPException(status_code=409, detail="Username already exists")
    api_key = create_user(payload.username)
    return {"username": payload.username, "api_key": api_key}