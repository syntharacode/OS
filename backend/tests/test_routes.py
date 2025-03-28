# Import FastAPI test client
from fastapi.testclient import TestClient

# Import the Synthara API server instance
from backend.api.server import app

# Initialize test client for the API
client = TestClient(app)

# Test the root "/" endpoint to verify API availability
def test_root():
    res = client.get("/")
    assert res.status_code == 200                    # Expect HTTP 200 OK
    assert res.json() == {"message": "Synthara OS is running."}  # Verify correct message

# Test the /api/llm/query endpoint with a sample prompt
def test_llm_query():
    res = client.post("/api/llm/query", json={"input": "What is Web3?"})
    assert res.status_code == 200                    # Expect HTTP 200 OK
    assert "response" in res.json()                  # Ensure response is present in output

# Test the /api/llm/train endpoint with training data
def test_train_endpoint():
    res = client.post("/api/llm/train", json={"texts": ["Define blockchain in one line."]})
    assert res.status_code == 200                    # Expect HTTP 200 OK
    assert res.json().get("status") == "success"     # Verify successful training response
