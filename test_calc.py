import pytest
import calc


def test_add():
    assert calc.add(20, 10) == 30
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0
    assert calc.add(-1, -1) == -2


def test_subtract():
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, 1)  == -2
    assert calc.subtract(-1, -1) == 0

def test_multiply():
    assert calc.multiply(10, 5) == 50
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-1, -1) == 1

def test_divide():
    assert calc.divide(10, 5) == 2
    assert calc.divide(-1, 1) == -1
    assert calc.divide(-1, -1) == 1
    assert calc.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_modulus():
    assert calc.modulus(10, 5) == 0
    assert calc.modulus(-1, 1) == 0
    assert calc.modulus(-1, -1) == 0
    assert calc.modulus(5, 2) == 1
    with pytest.raises(ValueError):
        calc.modulus(10, 0)