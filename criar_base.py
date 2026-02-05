import sqlite3

conn = sqlite3.connect("basededados.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS utilizadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")
conn.commit()

cursor.execute("DELETE FROM utilizadores")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='utilizadores'")
conn.commit()

utilizadores = [
    "Isaac Mendes",
    "Victor Carneiro",
    "Tiago Martins",
    "Caio Brito",
    "David Lemos",
    "Diego Andrade"
]

for nome in utilizadores:
    cursor.execute("INSERT INTO utilizadores (nome) VALUES (?)", (nome,))

conn.commit()

cursor.execute("SELECT * FROM utilizadores")
for linha in cursor.fetchall():
    print(linha)

conn.close()