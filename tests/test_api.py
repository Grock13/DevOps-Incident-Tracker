from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_incidents():
    response = client.get("/incidents")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_incident():
    response = client.post(
        "/incidents",
        json={
            "service": "EC2",
            "status": "open",
            "summary": "SSH timeout"
        }
    )

    assert response.status_code == 201
    assert response.json()["service"] == "EC2"
