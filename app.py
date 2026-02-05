from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
import json
from pathlib import Path

app = FastAPI(title="API de Utilizadores (JSON-LD)")

CAMINHO_JSONLD = Path("data/utilizadores.jsonld")


def carregar_dados():
    """Carrega os dados do ficheiro JSON-LD"""
    with open(CAMINHO_JSONLD, encoding="utf-8") as f:
        return json.load(f)


@app.get("/utilizadores")
def listar_utilizadores():
    """Devolve todos os utilizadores em JSON-LD formatado"""
    dados = carregar_dados()
    conteudo_formatado = json.dumps(dados, indent=2, ensure_ascii=False)
    return Response(
        content=conteudo_formatado,
        media_type="application/ld+json"
    )


@app.get("/utilizadores/{utilizador_id}")
def obter_utilizador(utilizador_id: str):
    """Devolve um utilizador pelo ID"""
    dados = carregar_dados()
    for utilizador in dados["itemListElement"]:
        if utilizador["@id"] == utilizador_id:
            conteudo_formatado = json.dumps(utilizador, indent=2, ensure_ascii=False)
            return Response(
                content=conteudo_formatado,
                media_type="application/ld+json"
            )
    raise HTTPException(status_code=404, detail="Utilizador não encontrado")

CAMINHO_ESCOLAS = Path("data/escolas.jsonld")

def carregar_escolas():
    with open(CAMINHO_ESCOLAS, encoding="utf-8") as f:
        return json.load(f)

@app.get("/escolas")
def listar_escolas():
    """Devolve todas as escolas em JSON-LD formatado"""
    dados = carregar_escolas()
    conteudo_formatado = json.dumps(dados, indent=2, ensure_ascii=False)
    return Response(
        content=conteudo_formatado,
        media_type="application/ld+json"
    )