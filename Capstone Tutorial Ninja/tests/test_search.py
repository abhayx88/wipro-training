from pages.search_page import SearchPage


def test_search_product(driver):

    search = SearchPage(driver)

    search.search_product("iphone")

    assert "Search" in driver.title

    search.open_first_product()

    assert "iPhone" in driver.page_source
