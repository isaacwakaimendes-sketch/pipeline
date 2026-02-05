import json
from pathlib import Path
from tabulate import tabulate

CAMINHO_UTILIZADORES = Path("data/utilizadores.jsonld")
CAMINHO_ESCOLAS = Path("data/escolas.jsonld")

def ver_utilizadores():
    with open(CAMINHO_UTILIZADORES, encoding="utf-8") as f:
        dados = json.load(f)
    
    tabela = []
    for u in dados["utilizadores"]:
        tabela.append([
            u.get("id"),
            u.get("name"),
            u.get("age"),
            u.get("email"),
            u.get("id_escola"),
            u.get("ano"),
            u.get("curso"),
            "Sim" if u.get("estagiario") else "Não"
        ])
    
    headers = ["ID", "Nome", "Idade", "Email", "Escola ID", "Ano", "Curso", "Estagiário"]
    print(tabulate(tabela, headers=headers, tablefmt="grid"))

def ver_escolas():
    with open(CAMINHO_ESCOLAS, encoding="utf-8") as f:
        dados = json.load(f)
    
    tabela = []
    for e in dados["escolas"]:
        coords = e["localizacao"]["geometry"]["coordinates"]
        tabela.append([
            e.get("id"),
            e.get("nome"),
            e.get("nivel"),
            e.get("ativa"),
            coords[1],  
            coords[0]   
        ])
    
    headers = ["ID", "Nome", "Nível", "Ativa", "Latitude", "Longitude"]
    print(tabulate(tabela, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    print("=== Utilizadores ===")
    ver_utilizadores()
    print("\n=== Escolas ===")
    ver_escolas()