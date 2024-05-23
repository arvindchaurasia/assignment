import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add():
    response = client.post("/addlist", json={
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    })
    assert response.status_code == 200
    assert response.json()["response"] == [3, 7]

def test_invalid_payload():
    response = client.post("/addlist", json={
        "batchid": "id0101",
        "payload": [[1, "a"], [3, 4]]
    })
    assert response.status_code == 400
    assert "All elements in each pair must be integers" in response.json()["detail"]


def test_non_list_payload():
    response = client.post("/addlist", json={
        "batchid": "id0101",
        "payload": "not a list"
    })
    assert response.status_code == 422  # Validation error for incorrect input type

