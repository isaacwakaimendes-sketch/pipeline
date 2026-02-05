from app import salvar_texto

def test_salvar_texto(tmp_path):
    arquivo = tmp_path / "teste.txt"
    salvar_texto("Olá, mundo!", arquivo)
    conteudo = arquivo.read_text(encoding="utf-8")
    assert conteudo == "Olá, mundo!"
