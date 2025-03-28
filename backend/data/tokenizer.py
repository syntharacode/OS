# Import the HuggingFace tokenizer loader
from transformers import AutoTokenizer

# Import SyntharaOS system configuration (e.g., model name)
from backend.core.config import settings

# Internal singleton instance for tokenizer (lazy-loaded once)
_tokenizer_instance = None

# Lazy-load tokenizer for reuse
# Loads the tokenizer on first call and reuses it afterward
def get_tokenizer():
    global _tokenizer_instance
    if _tokenizer_instance is None:
        print("[SyntharaOS] Loading tokenizer...")
        _tokenizer_instance = AutoTokenizer.from_pretrained(settings.MODEL_NAME)
    return _tokenizer_instance

# Tokenize input text and return PyTorch-compatible tensor dict
def tokenize_text(text: str) -> dict:
    tokenizer = get_tokenizer()
    return tokenizer(text, return_tensors="pt")
