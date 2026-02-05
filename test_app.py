import pytest
import sqlite3
from app import criar_tabela, adicionar_usuario, buscar_usuario

@pytest.fixture
def db_conn():
    """Cria uma conexão SQLite em memória antes de cada teste e fecha depois"""
    conn = sqlite3.connect("basededados.db")  
    criar_tabela(conn)
    yield conn
    conn.close()

def test_adicionar_e_buscar_usuario(db_conn):
    adicionar_usuario(db_conn, "Isaac")
    usuario = buscar_usuario(db_conn, "Isaac")
    assert usuario is not None
    assert usuario[1] == "Isaac"