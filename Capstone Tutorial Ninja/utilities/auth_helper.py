from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage


def login_or_register(driver, email, password):

    login = LoginPage(driver)
    login.open_login()
    login.login(email, password)

    # if login failed → register
    if "Warning" in driver.page_source:

        register = RegisterPage(driver)
        register.open_register()

        register.register_user(
            "Test",
            "User",
            email,
            password
        )

        # after register → auto login → logout → login fresh
        account = AccountPage(driver)
        account.logout()

        login.open_login()
        login.login(email, password)
