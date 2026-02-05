def salvar_texto(texto, arquivo):
    """Salva o texto no arquivo especificado."""
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(texto)
