from app import procurar_utilizador_por_nome

def test_procurar_utilizador_existente():
    utilizador = procurar_utilizador_por_nome("Isaac Mendes")
    assert utilizador is not None
    assert utilizador["name"] == "Isaac Mendes"

def test_procurar_utilizador_inexistente():
    utilizador = procurar_utilizador_por_nome("Nome Que Não Existe")
    assert utilizador is None