import sqlite3
import json

conn = sqlite3.connect("basededados.db")
cursor = conn.cursor()

cursor.execute("SELECT id, nome FROM utilizadores")
linhas = cursor.fetchall()

jsonld = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": []
}

for id_, nome in linhas:
    jsonld["itemListElement"].append({
        "@type": "Person",
        "@id": f"utilizador/{id_}",
        "name": nome
    })

conn.close()

with open("utilizadores.jsonld", "w", encoding="utf-8") as f:
    json.dump(jsonld, f, ensure_ascii=False, indent=2)

print("JSON-LD gerado com sucesso")