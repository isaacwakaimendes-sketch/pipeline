from app import soma, multiplica

def test_soma_multiplica():
    resultado = multiplica(soma(2, 3), 2)
    assert resultado == 10