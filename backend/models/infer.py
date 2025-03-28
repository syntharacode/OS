# Import PyTorch for inference execution
import torch

# Import the central Synthara engine to access the loaded model and tokenizer
from backend.core.engine import engine

# Generate a response from the current LLM based on the input prompt
def generate_response(prompt: str, max_tokens: int = 100, temperature: float = 0.7):
    # Retrieve model and tokenizer from Synthara engine
    llm = engine.get_model()
    model = llm["model"]
    tokenizer = llm["tokenizer"]

    # Tokenize the prompt and move it to the model's device (e.g. GPU or CPU)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    # Run model inference without tracking gradients (inference mode)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,     # Maximum number of tokens to generate
            temperature=temperature,       # Sampling temperature for randomness
            do_sample=True                 # Enable sampling for non-deterministic output
        )

    # Decode the generated tokens into a readable string
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded
