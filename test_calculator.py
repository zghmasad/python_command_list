import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    """Returns a Calculator instance"""
    return Calculator()


def test_initial_value(calculator):
    assert calculator.total == 0


def test_add_one(calculator):
    calculator.set(1)
    calculator.add()
    assert calculator.total == 1


def test_subtract_one(calculator):
    calculator.set(1)
    calculator.sub()
    assert calculator.total == -1


def test_add_one_and_one(calculator):
    calculator.set(1)
    calculator.add()
    calculator.set(1)
    calculator.add()
    assert calculator.total == 2
