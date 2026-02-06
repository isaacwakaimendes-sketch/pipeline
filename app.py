from fastapi import FastAPI, HTTPException, Body
from pathlib import Path
import json
from typing import List, Optional

app = FastAPI(title="API de Gestão Escolar", version="1.0.0")

CAMINHO_UTILIZADORES = Path("data/utilizadores.jsonld")
CAMINHO_ESCOLAS = Path("data/escolas.jsonld")

from pydantic import BaseModel

class UtilizadorUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    hobbies: Optional[List[str]] = None
    ativo: Optional[bool] = None
    id_escola: Optional[str] = None
    ano: Optional[str] = None
    curso: Optional[str] = None
    estagiario: Optional[bool] = None

def carregar_utilizadores():
    with open(CAMINHO_UTILIZADORES, encoding="utf-8") as f:
        return json.load(f)

def salvar_utilizadores(dados):
    with open(CAMINHO_UTILIZADORES, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def carregar_escolas():
    with open(CAMINHO_ESCOLAS, encoding="utf-8") as f:
        return json.load(f)

def salvar_escolas(dados):
    with open(CAMINHO_ESCOLAS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

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

@app.put("/utilizadores/{utilizador_id}")
def atualizar_utilizador_completo(utilizador_id: str, dados_atualizados: dict = Body(...)):
    dados = carregar_utilizadores()
    for i, u in enumerate(dados["utilizadores"]):
        if u["id"] == utilizador_id:
            dados_atualizados["id"] = utilizador_id
            dados["utilizadores"][i] = dados_atualizados
            salvar_utilizadores(dados)
            return {"mensagem": "Utilizador atualizado completamente"}
    raise HTTPException(status_code=404, detail="Utilizador não encontrado")

@app.patch("/utilizadores/{utilizador_id}")
def atualizar_utilizador_parcial(utilizador_id: str, dados_parciais: dict = Body(...)):
    dados = carregar_utilizadores()
    for i, u in enumerate(dados["utilizadores"]):
        if u["id"] == utilizador_id:
            dados["utilizadores"][i].update(dados_parciais)
            salvar_utilizadores(dados)
            return {
                "mensagem": "Utilizador atualizado parcialmente",
                "dados": dados["utilizadores"][i]
            }
    raise HTTPException(status_code=404, detail="Utilizador não encontrado")

@app.delete("/utilizadores/{utilizador_id}")
def remover_utilizador(utilizador_id: str):
    dados = carregar_utilizadores()
    for i, u in enumerate(dados["utilizadores"]):
        if u["id"] == utilizador_id:
            removido = dados["utilizadores"].pop(i)
            salvar_utilizadores(dados)
            return {
                "mensagem": "Utilizador removido com sucesso",
                "utilizador_removido": removido
            }
    raise HTTPException(status_code=404, detail="Utilizador não encontrado")

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

@app.post("/escolas")
def adicionar_escola(nova: dict = Body(...)):
    dados = carregar_escolas()
    nova["id"] = str(len(dados["escolas"]) + 1)
    dados["escolas"].append(nova)
    salvar_escolas(dados)
    return {"mensagem": "Escola adicionada", "id": nova["id"]}

@app.put("/escolas/{escola_id}")
def atualizar_escola_completo(escola_id: str, dados_atualizados: dict = Body(...)):
    dados = carregar_escolas()
    for i, e in enumerate(dados["escolas"]):
        if e["id"] == escola_id:
            dados_atualizados["id"] = escola_id
            dados["escolas"][i] = dados_atualizados
            salvar_escolas(dados)
            return {"mensagem": "Escola atualizada completamente"}
    raise HTTPException(status_code=404, detail="Escola não encontrada")

@app.patch("/escolas/{escola_id}")
def atualizar_escola_parcial(escola_id: str, dados_parciais: dict = Body(...)):
    dados = carregar_escolas()
    for i, e in enumerate(dados["escolas"]):
        if e["id"] == escola_id:
            dados["escolas"][i].update(dados_parciais)
            salvar_escolas(dados)
            return {
                "mensagem": "Escola atualizada parcialmente",
                "dados": dados["escolas"][i]
            }
    raise HTTPException(status_code=404, detail="Escola não encontrada")

@app.delete("/escolas/{escola_id}")
def remover_escola(escola_id: str):
    dados = carregar_escolas()
    for i, e in enumerate(dados["escolas"]):
        if e["id"] == escola_id:
            removida = dados["escolas"].pop(i)
            salvar_escolas(dados)
            return {
                "mensagem": "Escola removida com sucesso",
                "escola_removida": removida
            }
    raise HTTPException(status_code=404, detail="Escola não encontrada")