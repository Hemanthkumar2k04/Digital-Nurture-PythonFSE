import pytest
from src.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add_positive_numbers(calc):
    assert calc.add(2, 3) == 5


def test_divide_happy_path(calc):
    assert calc.divide(10, 2) == 5.0


def test_divide_by_sero_raises_error(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


def test_memory_starts_at_zero(calc):
    assert calc.get_memory() == 0


def test_add_to_memory(calc):
    calc.add_to_memory(5)
    assert calc.get_memory() == 5.0


def test_clear_memory(calc):
    calc.add_to_memory(10)
    calc.clear_memory()
    assert calc.get_memory() == 0
