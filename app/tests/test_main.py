from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data["app_name"] == "platform-api"
    assert data["version"] == "v1.0.0"
    assert "message" in data


def test_health():
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"


def test_version():
    response = client.get("/version")
    assert response.status_code == 200

    data = response.json()
    assert data["version"] == "v1.0.0"