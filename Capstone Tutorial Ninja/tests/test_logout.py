from pages.login_page import LoginPage
from pages.account_page import AccountPage


def test_logout(driver):

    login = LoginPage(driver)
    login.open_login()
    login.login("abhay+1@gmail.com", "Test@123")   # use your password

    account = AccountPage(driver)
    account.logout()

    assert "Account Logout" in driver.page_source
