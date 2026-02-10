import json
from pathlib import Path

ficheiros = [
    Path("data/utilizadores.jsonld"),
    Path("data/escolas.jsonld")
]

for ficheiro in ficheiros:
    try:
        with open(ficheiro, encoding="utf-8") as f:
            json.load(f)
        print(f"[OK] {ficheiro} é um JSON válido")
    except json.JSONDecodeError as e:
        raise Exception(f"[ERRO] {ficheiro} não é um JSON válido: {e}")
    except FileNotFoundError:
        raise Exception(f"[ERRO] Ficheiro não encontrado: {ficheiro}")

print("Todos os ficheiros JSON-LD são válidos ✅")