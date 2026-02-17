import pytest
from utilities.driver_factory import get_driver
from utilities.config_reader import get_url


@pytest.fixture
def driver():

    driver = get_driver()
    driver.get(get_url())

    yield driver

    driver.quit()
