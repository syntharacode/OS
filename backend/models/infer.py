import torch
from backend.core.engine import engine
from backend.data.cleaner import full_clean  # NEU

def generate_response(prompt: str, max_tokens: int = 100, temperature: float = 0.7):
    llm = engine.get_model()
    model = llm["model"]
    tokenizer = llm["tokenizer"]

    prompt = full_clean(prompt)  # OPTIONAL CLEANING BEFORE INFERENCE

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=temperature,
            do_sample=True,
        )
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded
