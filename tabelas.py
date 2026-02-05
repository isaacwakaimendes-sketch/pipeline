import json
from pathlib import Path
from tabulate import tabulate

BASE_DIR = Path(__file__).parent

CAMINHO_UTILIZADORES = BASE_DIR / "data" / "utilizadores.jsonld"
CAMINHO_ESCOLAS = BASE_DIR / "data" / "escolas.jsonld"

def truncate(text, max_len=20):
    text = str(text)
    return text if len(text) <= max_len else text[:max_len-3] + "..."

def ver_utilizadores():
    if not CAMINHO_UTILIZADORES.exists():
        print(f"Erro: ficheiro {CAMINHO_UTILIZADORES} não encontrado!")
        return

    try:
        with open(CAMINHO_UTILIZADORES, encoding="utf-8") as f:
            dados = json.load(f)
    except Exception as e:
        print("Erro ao ler utilizadores:", e)
        return
    
    tabela = []
    for u in dados.get("utilizadores", []):
        tabela.append([
            u.get("id"),
            truncate(u.get("name"), 15),
            u.get("age"),
            truncate(u.get("email"), 20),
            u.get("id_escola"),
            u.get("ano"),
            truncate(u.get("curso"), 25),
            "Sim" if u.get("estagiario") else "Não"
        ])
    
    headers = ["ID", "Nome", "Idade", "Email", "Escola ID", "Ano", "Curso", "Estágio"]
    print(tabulate(tabela, headers=headers, tablefmt="grid"))

def ver_escolas():
    if not CAMINHO_ESCOLAS.exists():
        print(f"Erro: ficheiro {CAMINHO_ESCOLAS} não encontrado!")
        return

    try:
        with open(CAMINHO_ESCOLAS, encoding="utf-8") as f:
            dados = json.load(f)
    except Exception as e:
        print("Erro ao ler escolas:", e)
        return
    
    tabela = []
    for e in dados.get("escolas", []):
        coords = e.get("localizacao", {}).get("geometry", {}).get("coordinates", [None, None])
        tabela.append([
            e.get("id"),
            truncate(e.get("nome"), 25),
            e.get("nivel"),
            "S" if e.get("ativa") else "N",
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