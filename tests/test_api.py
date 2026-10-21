from fastapi.testclient import TestClient
from app.main import app


def test_health():
    with TestClient(app) as client:
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json()["database"] == "connected"


def test_get_incidents():
    with TestClient(app) as client:
        response = client.get("/incidents")

        assert response.status_code == 200
        assert isinstance(response.json(), list)


def test_create_incident():
    with TestClient(app) as client:
        response = client.post(
            "/incidents",
            json={
                "service": "Docker",
                "status": "open",
                "summary": "Database integration test"
            }
        )

        assert response.status_code == 201

        incident_id = response.json()["id"]

        incidents = client.get("/incidents").json()

        assert any(
            item["id"] == incident_id
            for item in incidents
        )
