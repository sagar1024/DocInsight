from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to DocInsight"}

def test_upload_file():
    files = {"file": ("test_document.pdf", b"This is a test document", "application/pdf")}
    response = client.post("/summarize/upload", files=files)
    assert response.status_code == 200
    assert "summary" in response.json()

def test_chatbot_query():
    payload = {"query": "What is the purpose of DocInsight?"}
    response = client.post("/chatbot/query", json=payload)
    assert response.status_code == 200
    assert "response" in response.json()
