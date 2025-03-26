from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.models.trainer import fine_tune_model

router = APIRouter()

class TrainPayload(BaseModel):
    texts: list[str]

@router.post("/api/llm/train")
async def train_llm(payload: TrainPayload):
    if not payload.texts or not isinstance(payload.texts, list):
        raise HTTPException(status_code=400, detail="Invalid training data")

    try:
        fine_tune_model(payload.texts)
        return {"status": "success", "message": "Model fine-tuned successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))