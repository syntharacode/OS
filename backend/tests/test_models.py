from backend.models.loader import load_model
from backend.models.infer import generate_response


def test_load_model():
    llm = load_model()
    assert "model" in llm
    assert "tokenizer" in llm

def test_generate_response():
    prompt = "What is Web3?"
    response = generate_response(prompt)
    assert isinstance(response, str)
    assert len(response.strip()) > 0