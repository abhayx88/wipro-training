import pytest
from .calculator import add, divide

# ---------- xUnit STYLE SETUP / TEARDOWN ----------

def setup_module(module):
    print("\n[setup_module] Runs once before module tests")


def teardown_module(module):
    print("\n[teardown_module] Runs once after module tests")


def setup_function(function):
    print("\n[setup_function] Runs before each test")


def teardown_function(function):
    print("\n[teardown_function] Runs after each test")


# ---------- TESTS USING FIXTURES ----------

def test_addition(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 12


def test_division(sample_numbers, module_resource):
    a, b = sample_numbers
    assert divide(a, b) == 5


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
