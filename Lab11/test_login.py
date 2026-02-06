from Lab11.login_pom_factory import Login


def test_login(driver):

    login = Login(driver)

    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    assert login.verify_dashboard()
