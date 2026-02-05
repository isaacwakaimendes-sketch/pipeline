import pytest
from app import divide

def test_divide_por_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
