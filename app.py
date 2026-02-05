import sqlite3

def criar_tabela(conn):
    """Cria uma tabela de usuários"""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)
    conn.commit()

def adicionar_usuario(conn, nome):
    """Adiciona um usuário"""
    conn.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()

def buscar_usuario(conn, nome):
    """Busca um usuário pelo nome"""
    cursor = conn.execute("SELECT id, nome FROM usuarios WHERE nome = ?", (nome,))
    return cursor.fetchone()