# test_app.py
from app import salvar_texto

def test_salvar_texto(tmp_path):
    # Cria um arquivo temporário chamado teste.txt
    arquivo = tmp_path / "teste.txt"
    
    # Chama a função que queremos testar
    salvar_texto("Olá, mundo!", arquivo)
    
    # Lê o conteúdo do arquivo e verifica se está correto
    conteudo = arquivo.read_text(encoding="utf-8")
    assert conteudo == "Olá, mundo!"
