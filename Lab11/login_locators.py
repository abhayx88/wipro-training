from selenium.webdriver.common.by import By


class LoginLocators:

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    DASHBOARD = (By.XPATH, "//h6[text()='Dashboard']")
