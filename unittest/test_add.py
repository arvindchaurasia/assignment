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


def test_empty_payload():
    response = client.post("/addlist", json={
        "batchid": "id0101",
        "payload": []
    })
    assert response.status_code == 200
    assert response.json()["response"] == []

def test_non_list_payload():
    response = client.post("/addlist", json={
        "batchid": "id0101",
        "payload": "not a list"
    })
    assert response.status_code == 422  # Validation error for incorrect input type

