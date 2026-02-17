import pytest

@pytest.mark.smoke
@pytest.mark.order(1)
def test_open_site(driver):

    # verify homepage loaded
    assert "Your Store" in driver.title
