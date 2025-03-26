from transformers import AutoModelForCausalLM, AutoTokenizer
from backend.models.adapter import apply_adapter
import torch
from backend.core.config import settings

MODEL_NAME = settings.MODEL_NAME

def load_model():
    print("[SyntharaOS] Loading language model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    model = apply_adapter(model)
    model.eval()

    if torch.cuda.is_available():
        model = model.to("cuda")
        print("[SyntharaOS] Model loaded on CUDA")
    else:
        print("[SyntharaOS] Model running on CPU")

    return {"model": model, "tokenizer": tokenizer}
