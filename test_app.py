import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_listar_utilizadores():
    response = client.get("/utilizadores")
    assert response.status_code == 200
    dados = response.json()
    assert "utilizadores" in dados
    assert len(dados["utilizadores"]) == 5

def test_obter_utilizador():
    response = client.get("/utilizadores/1")
    assert response.status_code == 200
    u = response.json()
    assert u["name"] == "Isaac Mendes"
    assert "email" in u
    assert "id_escola" in u

def test_listar_escolas():
    response = client.get("/escolas")
    assert response.status_code == 200
    dados = response.json()
    assert "escolas" in dados
    assert len(dados["escolas"]) == 3

def test_obter_escola():
    response = client.get("/escolas/1")
    assert response.status_code == 200
    e = response.json()
    assert e["nome"] == "Escola Secundária da Senhora da Hora"
    assert "localizacao" in e