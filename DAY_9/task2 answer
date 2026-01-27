Introduction

Unit testing focuses on testing individual units or functions of an application.
Test Driven Development (TDD) is a development approach where tests are written before the actual code.

Requirement 1: Write Unit Test Cases First (TDD – Red Stage)

We first write failing tests for calculator operations before implementing any logic.

Using pytest
📄 tests/test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

def test_addition():
    assert add(2, 3) == 5

def test_subtraction():
    assert subtract(5, 2) == 3

def test_multiplication():
    assert multiply(4, 3) == 12

def test_division():
    assert divide(10, 2) == 5

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


🔴 At this stage, tests fail because the functions do not exist.

Requirement 2: Use a Python Unit Testing Framework

We use pytest as the unit testing framework because it:

Has simple syntax

Supports exception testing

Provides clear test reports

Requirement 3: Implement Calculator Functions (Green Stage)

Now we write the minimum code required to make tests pass.

📄 calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


🟢 Now all tests pass successfully.

Requirement 4: Handling Edge Cases
Edge Case: Division by Zero

Dividing by zero raises a ValueError

Tested using pytest.raises()

with pytest.raises(ValueError):
    divide(10, 0)


✔ Ensures application does not crash unexpectedly.

Requirement 5: Explain the TDD Cycle (Red → Green → Refactor)
🔴 Red

Write test cases first

Tests fail because functionality is missing

🟢 Green

Write minimal code to pass tests

Focus only on correctness

🔵 Refactor

Improve code structure and readability

Ensure tests still pass

No change in behavior