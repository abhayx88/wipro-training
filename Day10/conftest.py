import pytest

# Function-scoped fixture
@pytest.fixture(scope="function")
def sample_numbers():
    return (10, 2)

# Module-scoped fixture
@pytest.fixture(scope="module")
def module_resource():
    print("\n[Setup] Module resource created")
    yield "RESOURCE"
    print("\n[Teardown] Module resource destroyed")
