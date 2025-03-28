# Import the response generation function from the Synthara inference module
from backend.models.infer import generate_response

# Unit test for basic prompt inference
def test_infer_basic():
    # Define a sample input prompt
    prompt = "Explain the function of a smart contract."

    # Generate a response using the Synthara LLM
    result = generate_response(prompt)

    # Ensure the result is a string
    assert isinstance(result, str)

    # Ensure the result is not empty or whitespace-only
    assert len(result.strip()) > 0
