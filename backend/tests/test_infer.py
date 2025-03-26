from backend.models.infer import generate_response


def test_infer_basic():
    prompt = "Explain the function of a smart contract."
    result = generate_response(prompt)
    assert isinstance(result, str)
    assert len(result.strip()) > 0