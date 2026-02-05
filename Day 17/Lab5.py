from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -----------------------------
# Helper Functions (ADD THIS)
# -----------------------------

def slow_type(element, text, delay=0.12):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

def highlight(driver, element):
    driver.execute_script(
        "arguments[0].style.border='3px solid red'", element)
    time.sleep(0.3)

# -----------------------------
# Launch Application
# -----------------------------
driver = webdriver.Firefox()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.get("https://tutorialsninja.com/demo/")

assert "Your Store" in driver.title
print("Title Verified")

# -----------------------------
# My Account → Register
# -----------------------------
my_account = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']"))
)
highlight(driver, my_account)
my_account.click()

register = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
)
highlight(driver, register)
register.click()

heading = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h1[text()='Register Account']"))
)

assert heading.text == "Register Account"
print("Register Page Verified")

time.sleep(1)  # Let examiner see page

# -----------------------------
# Click Continue (No Data)
# -----------------------------
continue_btn = driver.find_element(By.XPATH, "//input[@value='Continue']")
highlight(driver, continue_btn)
continue_btn.click()

warning = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
)

assert "Privacy Policy" in warning.text
print("Warning Message Verified")

# -----------------------------
# PERSONAL DETAILS
# -----------------------------

first_name = driver.find_element(By.ID, "input-firstname")
highlight(driver, first_name)

slow_type(first_name, "A"*33)
first_name.clear()
slow_type(first_name, "Abhay")

last_name = driver.find_element(By.ID, "input-lastname")
highlight(driver, last_name)

slow_type(last_name, "B"*33)
last_name.clear()
slow_type(last_name, "Gupta")

email = f"test{int(time.time())}@mail.com"
email_box = driver.find_element(By.ID, "input-email")
highlight(driver, email_box)
slow_type(email_box, email)

telephone_box = driver.find_element(By.ID, "input-telephone")
highlight(driver, telephone_box)
slow_type(telephone_box, "1234567")

print("Personal Details Completed")

# -----------------------------
# PASSWORD
# -----------------------------
password_box = driver.find_element(By.ID, "input-password")
highlight(driver, password_box)
slow_type(password_box, "Test@123")

confirm_box = driver.find_element(By.ID, "input-confirm")
highlight(driver, confirm_box)
slow_type(confirm_box, "Test@123")

print("Password Entered")

# -----------------------------
# NEWSLETTER + PRIVACY
# -----------------------------
newsletter = driver.find_element(By.XPATH, "//label[normalize-space()='Yes']")
highlight(driver, newsletter)
newsletter.click()

privacy = driver.find_element(By.NAME, "agree")
highlight(driver, privacy)
privacy.click()

time.sleep(1)  # Examiner can see filled form

# -----------------------------
# Continue
# -----------------------------
continue_final = driver.find_element(By.XPATH, "//input[@value='Continue']")
highlight(driver, continue_final)
continue_final.click()

success_msg = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]")
    )
)

assert success_msg.is_displayed()
print("Account Created Successfully!")

driver.find_element(By.LINK_TEXT, "Continue").click()

# -----------------------------
# Order History
# -----------------------------
order_history = driver.find_element(By.LINK_TEXT, "Order History")
highlight(driver, order_history)
order_history.click()

assert "Order History" in driver.page_source
print("Order History Verified")

time.sleep(3)
driver.quit()
