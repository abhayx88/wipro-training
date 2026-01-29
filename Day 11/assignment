'''

1️⃣ Assert Statements and Exceptions
✅ Simple assert
def test_addition():
    assert 2 + 3 == 5
❌ Assert with message
def test_subtraction():
    assert 5 - 3 == 1, "Subtraction result is incorrect"
🚨 Exception handling (pytest.raises)
import pytest

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

2️⃣ Pytest Command Line Arguments
Run all tests
pytest
Run a specific file
pytest test_math.py
Run a specific test
pytest test_math.py::test_addition
Verbose output
pytest -v
Show print statements
pytest -s

3️⃣ Customizing Tests with Command Line & Config Files
📄 pytest.ini
[pytest]
addopts = -v -s
testpaths = tests
markers =
    smoke: smoke tests
    regression: regression tests
Using custom marker
import pytest

@pytest.mark.smoke
def test_login():
    assert True
Run smoke tests only
pytest -m smoke

4️⃣ Handling Skips and Expected Failures
⏭ Skip test
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment():
    assert True
⏭ Conditional skip
import sys
import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only():
    assert True
⚠ Expected failure (xfail)
import pytest

@pytest.mark.xfail(reason="Known bug")
def test_known_issue():
    assert 2 * 2 == 5

5️⃣ Distributed and Parallel Tests (pytest-xdist)
Install
pip install pytest-xdist
Run tests in parallel (4 CPUs)
pytest -n 4
Distributed load
pytest -n auto

6️⃣ Reporting Test Results & Tracking History
📄 Generate HTML report
pip install pytest-html
pytest --html=report.html --self-contained-html
📊 JUnit XML report (CI/CD)
pytest --junitxml=results.xml

7️⃣ Writing and Running Unit Tests
Function to test
# calculator.py
def multiply(a, b):
    return a * b
Unit test
# test_calculator.py
from calculator import multiply

def test_multiply():
    assert multiply(3, 4) == 12
Run
pytest test_calculator.py

8️⃣ Writing Functional Tests
Example: Login validation function
# auth.py
def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Invalid Credentials"
Functional test
# test_auth.py
def test_valid_login():
    assert login("admin", "admin123") == "Login Successful"

def test_invalid_login():
    assert login("user", "wrong") == "Invalid Credentials"

📂 Recommended Project Structure
project/
│
├── tests/
│   ├── test_calculator.py
│   ├── test_auth.py
│
├── calculator.py
├── auth.py
├── pytest.ini

'''