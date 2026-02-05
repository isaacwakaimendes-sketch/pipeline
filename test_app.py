import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_utilizadores():
    response = client.get("/utilizadores")
    assert response.status_code == 200
    data = response.json()
    assert "utilizadores" in data
    assert len(data["utilizadores"]) > 0

def test_get_escolas():
    response = client.get("/escolas")
    assert response.status_code == 200
    data = response.json()
    assert "escolas" in data
    assert len(data["escolas"]) > 0

def test_post_utilizador():
    novo = {
        "name": "Teste API",
        "age": 20,
        "email": "teste@example.com",
        "hobbies": ["programação"],
        "ativo": True,
        "id_escola": "1",
        "ano": "12",
        "curso": "Teste",
        "estagiario": False
    }
    response = client.post("/utilizadores", json=novo)
    assert response.status_code == 200
    result = response.json()
    assert "mensagem" in result
    assert "id" in result