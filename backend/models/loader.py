# Import HuggingFace transformer model and tokenizer classes
from transformers import AutoModelForCausalLM, AutoTokenizer

# Import optional model adapter layer (e.g., LoRA, quantization)
from backend.models.adapter import apply_adapter

# Import PyTorch for device detection and tensor control
import torch

# Load SyntharaOS system settings (e.g., model path or HuggingFace ID)
from backend.core.config import settings

# Get the model name or path from settings
MODEL_NAME = settings.MODEL_NAME

# Load the language model and tokenizer, apply adapters, and move to appropriate device
def load_model():
    print("[SyntharaOS] Loading language model...")

    # Load tokenizer and model from HuggingFace model hub or local path
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

    # Optionally wrap model with adapter logic (e.g., LoRA, quantization, etc.)
    model = apply_adapter(model)

    # Set model to inference mode
    model.eval()

    # Move model to GPU if available, else run on CPU
    if torch.cuda.is_available():
        model = model.to("cuda")
        print("[SyntharaOS] Model loaded on CUDA")
    else:
        print("[SyntharaOS] Model running on CPU")

    # Return both model and tokenizer in a reusable dict
    return {"model": model, "tokenizer": tokenizer}
