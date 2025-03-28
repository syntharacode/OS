# Import FastAPI router and HTTP error handling
from fastapi import APIRouter, HTTPException

# Import Pydantic base model for request validation
from pydantic import BaseModel

# Import user service logic for creating and retrieving users
from backend.services.user_service import create_user, get_user_by_name

# Initialize API router instance
router = APIRouter()

# Define expected payload structure for user creation
class CreateUserPayload(BaseModel):
    username: str

# API endpoint for creating a new user
@router.post("/api/user/create")
async def create_user_endpoint(payload: CreateUserPayload):
    # Check if the username already exists in the system
    if get_user_by_name(payload.username):
        raise HTTPException(status_code=409, detail="Username already exists")

    # Create user and return the new API key
    api_key = create_user(payload.username)
    return {"username": payload.username, "api_key": api_key}
