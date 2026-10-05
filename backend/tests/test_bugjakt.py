from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_delete_item_updates_stats() -> None:
    client.post("/api/items", json={"text": "milk"})

    bread = client.post("/api/items", json={"text": "bread"}).json()

    response = client.delete(f"/api/items/{bread['id']}")
    assert response.status_code == 204

    response = client.get("/api/items/stats")
    assert response.status_code == 200
    assert response.json() == {
        "count": 1,
        "total_characters": 4,
    }