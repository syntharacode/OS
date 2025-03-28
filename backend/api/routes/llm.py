# Import FastAPI router and request context
from fastapi import APIRouter, Request

# Import Pydantic for validating incoming payloads
from pydantic import BaseModel

# Import global engine instance (provides access to model and DB)
from backend.core.engine import engine

# PyTorch for tensor operations and inference control
import torch

# Create a FastAPI router for LLM-related endpoints
router = APIRouter()

# Define expected input payload for querying the model
class QueryPayload(BaseModel):
    input: str                  # User input prompt
    max_tokens: int = 100       # Max tokens to generate in response
    temperature: float = 0.7    # Sampling temperature for variability

# POST endpoint to query the language model
@router.post("/api/llm/query")
async def query_llm(payload: QueryPayload):
    # Retrieve model and tokenizer from the Synthara engine
    llm = engine.get_model()
    model = llm["model"]
    tokenizer = llm["tokenizer"]

    # Tokenize user input and move it to the model's device (e.g. CPU or GPU)
    inputs = tokenizer(payload.input, return_tensors="pt").to(model.device)

    # Generate a response without computing gradients (inference-only)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=payload.max_tokens,
            temperature=payload.temperature,
            do_sample=True
        )

    # Decode the model output into human-readable text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}
