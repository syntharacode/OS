from fastapi import APIRouter, Request
from pydantic import BaseModel
from backend.core.engine import engine
import torch

router = APIRouter()

class QueryPayload(BaseModel):
    input: str
    max_tokens: int = 100
    temperature: float = 0.7

@router.post("/api/llm/query")
async def query_llm(payload: QueryPayload):
    llm = engine.get_model()
    model = llm["model"]
    tokenizer = llm["tokenizer"]

    inputs = tokenizer(payload.input, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=payload.max_tokens,
            temperature=payload.temperature,
            do_sample=True
        )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}