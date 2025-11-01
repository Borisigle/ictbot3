from fastapi.testclient import TestClient

from ict_backend.app import create_app


def test_health_endpoint_returns_ok_status() -> None:
    client = TestClient(create_app())

    response = client.get("/api/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["environment"]
    assert payload["application"]
    assert "timestamp" in payload
