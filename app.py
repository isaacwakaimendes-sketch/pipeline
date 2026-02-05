from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
import json
from pathlib import Path

app = FastAPI(title="API JSON-LD de Utilizadores e Escolas")

CAMINHO_UTILIZADORES = Path("data/utilizadores.jsonld")
CAMINHO_ESCOLAS = Path("data/escolas.jsonld")


def carregar_utilizadores():
    with open(CAMINHO_UTILIZADORES, encoding="utf-8") as f:
        return json.load(f)


def carregar_escolas():
    with open(CAMINHO_ESCOLAS, encoding="utf-8") as f:
        return json.load(f)


@app.get("/utilizadores")
def listar_utilizadores():
    """Devolve todos os utilizadores formatados"""
    dados = carregar_utilizadores()
    conteudo_formatado = json.dumps(dados, indent=2, ensure_ascii=False)
    return Response(content=conteudo_formatado, media_type="application/ld+json")


@app.get("/utilizadores/{utilizador_id}")
def obter_utilizador(utilizador_id: str):
    dados = carregar_utilizadores()
    for u in dados["utilizadores"]:
        if u["id"] == utilizador_id:
            conteudo_formatado = json.dumps(u, indent=2, ensure_ascii=False)
            return Response(content=conteudo_formatado, media_type="application/ld+json")
    raise HTTPException(status_code=404, detail="Utilizador não encontrado")


@app.get("/escolas")
def listar_escolas():
    """Devolve todas as escolas formatadas"""
    dados = carregar_escolas()
    conteudo_formatado = json.dumps(dados, indent=2, ensure_ascii=False)
    return Response(content=conteudo_formatado, media_type="application/ld+json")


@app.get("/escolas/{escola_id}")
def obter_escola(escola_id: str):
    dados = carregar_escolas()
    for e in dados["escolas"]:
        if e["id"] == escola_id:
            conteudo_formatado = json.dumps(e, indent=2, ensure_ascii=False)
            return Response(content=conteudo_formatado, media_type="application/ld+json")
    raise HTTPException(status_code=404, detail="Escola não encontrada")