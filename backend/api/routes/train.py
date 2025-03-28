# Import FastAPI tools for routing and exception handling
from fastapi import APIRouter, HTTPException

# Import Pydantic for validating the request payload
from pydantic import BaseModel

# Import fine-tuning function from the model trainer module
from backend.models.trainer import fine_tune_model

# Create a new FastAPI router instance
router = APIRouter()

# Define expected input payload for model fine-tuning
class TrainPayload(BaseModel):
    texts: list[str]  # A list of training samples (prompts, responses, etc.)

# POST endpoint to trigger model fine-tuning
@router.post("/api/llm/train")
async def train_llm(payload: TrainPayload):
    # Validate that the payload contains a non-empty list of texts
    if not payload.texts or not isinstance(payload.texts, list):
        raise HTTPException(status_code=400, detail="Invalid training data")

    try:
        # Execute model fine-tuning with the provided training texts
        fine_tune_model(payload.texts)
        return {"status": "success", "message": "Model fine-tuned successfully."}
    except Exception as e:
        # Handle any internal error and return a 500 response
        raise HTTPException(status_code=500, detail=str(e))
