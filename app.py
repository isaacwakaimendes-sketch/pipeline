import json
from pathlib import Path

CAMINHO_JSONLD = Path("data/utilizadores.jsonld")

def carregar_utilizadores():
    """Carrega utilizadores a partir de um ficheiro JSON-LD"""
    with open(CAMINHO_JSONLD, encoding="utf-8") as f:
        dados = json.load(f)
    return dados["itemListElement"]

def procurar_utilizador_por_nome(nome):
    """Procura um utilizador pelo nome"""
    utilizadores = carregar_utilizadores()
    for utilizador in utilizadores:
        if utilizador["name"] == nome:
            return utilizador
    return None