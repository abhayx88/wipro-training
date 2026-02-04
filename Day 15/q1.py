from selenium import webdriver
import time

# Open Chrome Browser
driver = webdriver.Chrome()

try:
    # Navigate to website
    driver.get("https://www.selenium.dev")

    # Wait for page to load
    time.sleep(2)

    # Print Page Title and URL
    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

finally:
    # Close the browser
    driver.quit()
