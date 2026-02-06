from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Day18.Login_PageFactory import loginpage_PageFactory

driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

loginobj = loginpage_PageFactory(driver)

loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")
loginobj.clicklogin()
