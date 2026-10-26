import pytest

from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["database"] == "connected"


def test_get_incidents(client):
    response = client.get("/incidents")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_incident(client):
    response = client.post(
        "/incidents",
        json={
            "service": "Docker",
            "status": "open",
            "summary": "CI integration test"
        }
    )

    assert response.status_code == 201

    incident_id = response.json()["id"]

    incidents = client.get("/incidents").json()

    assert any(
        item["id"] == incident_id
        for item in incidents
    )


def test_invalid_incident(client):
    response = client.post(
        "/incidents",
        json={
            "service": "EC2",
            "status": "open"
        }
    )

    assert response.status_code == 422
