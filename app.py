from fastapi import FastAPI, HTTPException, Body
from pathlib import Path
import json

app = FastAPI()

CAMINHO_UTILIZADORES = Path("data/utilizadores.jsonld")
CAMINHO_ESCOLAS = Path("data/escolas.jsonld")

def carregar_utilizadores():
    with open(CAMINHO_UTILIZADORES, encoding="utf-8") as f:
        return json.load(f)

def salvar_utilizadores(dados):
    with open(CAMINHO_UTILIZADORES, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def carregar_escolas():
    with open(CAMINHO_ESCOLAS, encoding="utf-8") as f:
        return json.load(f)

@app.get("/utilizadores")
def get_utilizadores():
    return carregar_utilizadores()

@app.get("/utilizadores/{utilizador_id}")
def get_utilizador(utilizador_id: str):
    dados = carregar_utilizadores()
    for u in dados["utilizadores"]:
        if u["id"] == utilizador_id:
            return u
    raise HTTPException(status_code=404, detail="Utilizador não encontrado")

@app.post("/utilizadores")
def adicionar_utilizador(novo: dict = Body(...)):
    dados = carregar_utilizadores()
    novo["id"] = str(len(dados["utilizadores"]) + 1)
    dados["utilizadores"].append(novo)
    salvar_utilizadores(dados)
    return {"mensagem": "Utilizador adicionado", "id": novo["id"]}

@app.get("/escolas")
def get_escolas():
    return carregar_escolas()

@app.get("/escolas/{escola_id}")
def get_escola(escola_id: str):
    dados = carregar_escolas()
    for e in dados["escolas"]:
        if e["id"] == escola_id:
            return e
    raise HTTPException(status_code=404, detail="Escola não encontrada")