import json
from pathlib import Path

caminho = Path("data/utilizadores.jsonld")
with open(caminho, encoding="utf-8") as f:
    dados = json.load(f)

print(json.dumps(dados, indent=2, ensure_ascii=False))