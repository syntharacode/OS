# Import Synthara OS model loading and inference functions
from backend.models.loader import load_model
from backend.models.infer import generate_response

# Test to ensure the model and tokenizer are properly loaded
def test_load_model():
    llm = load_model()
    assert "model" in llm         # Ensure the model key exists
    assert "tokenizer" in llm     # Ensure the tokenizer key exists

# Test to verify that the model generates a valid response to a simple prompt
def test_generate_response():
    prompt = "What is Web3?"                 # Example input prompt
    response = generate_response(prompt)     # Get LLM output

    assert isinstance(response, str)         # Check that result is a string
    assert len(response.strip()) > 0         # Ensure it's not empty or whitespace
