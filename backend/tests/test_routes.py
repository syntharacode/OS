from fastapi.testclient import TestClient
from backend.api.server import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Synthara OS is running."}

def test_llm_query():
    res = client.post("/api/llm/query", json={"input": "What is Web3?"})
    assert res.status_code == 200
    assert "response" in res.json()

def test_train_endpoint():
    res = client.post("/api/llm/train", json={"texts": ["Define blockchain in one line."]})
    assert res.status_code == 200
    assert res.json().get("status") == "success"