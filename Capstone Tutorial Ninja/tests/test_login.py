from pages.login_page import LoginPage


def test_login(driver):

    login = LoginPage(driver)

    login.open_login()

    login.login("abhay+1@gmail.com", "Test@123")   # ← use your real password here

    assert "My Account" in driver.title
