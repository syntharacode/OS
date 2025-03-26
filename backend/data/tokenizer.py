from transformers import AutoTokenizer
from backend.core.config import settings

_tokenizer_instance = None

# Lazy-load tokenizer for reuse

def get_tokenizer():
    global _tokenizer_instance
    if _tokenizer_instance is None:
        print("[SyntharaOS] Loading tokenizer...")
        _tokenizer_instance = AutoTokenizer.from_pretrained(settings.MODEL_NAME)
    return _tokenizer_instance


def tokenize_text(text: str) -> dict:
    tokenizer = get_tokenizer()
    return tokenizer(text, return_tensors="pt")