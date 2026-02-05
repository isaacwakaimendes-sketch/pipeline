from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_listar_utilizadores():
    response = client.get("/utilizadores")
    assert response.status_code == 200

    dados = response.json()
    assert "@context" in dados
    assert "itemListElement" in dados
    assert len(dados["itemListElement"]) == 6


def test_obter_utilizador_existente():
    response = client.get("/utilizadores/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Isaac Mendes"


def test_obter_utilizador_inexistente():
    response = client.get("/utilizadores/999")
    assert response.status_code == 404