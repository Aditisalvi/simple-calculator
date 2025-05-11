import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(3, 5) == -2

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6

def test_divide(calculator):
    assert calculator.divide(6, 2) == 3
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)
