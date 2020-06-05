from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# locators
LOG_IN_BTN_1 = (By.CSS_SELECTOR, "a.nav-eyebrow__login")
LOG_IN_BTN_2 = (By.CSS_SELECTOR, "button.ant-btn._1gF6tIm20jrHjFL8gIxetc.ant-btn-primary.ant-btn-lg")
NO_USER_NAME = (By.XPATH, "//div[contains(text(), 'Please enter your username.')]")
NO_PASSWORD = (By.XPATH, "//div[contains(text(), 'Please enter your password.')]")

# Open the url
driver.get( 'https://www.analyticpartners.com' )
sleep(2)

# Click Log In button_1
driver.find_element( *LOG_IN_BTN_1  ).click()

# Switch to next browser
driver.get( 'https://www.gpsenterprise.com/auth/login' )
sleep(2)

# Click Log In button_2
driver.find_element( *LOG_IN_BTN_2  ).click()

# Verify page has a text 'Invalid Login'
actual_text = driver.find_element( *NO_USER_NAME ).text
assert 'Please enter your username' in actual_text
print(f'Text is here: "{actual_text}" ')

# Verify page has a text 'Invalid Login'
actual_text = driver.find_element( *NO_PASSWORD ).text
assert 'Please enter your password' in actual_text
print(f'Text is here: "{actual_text}" ')

# Driver quit
driver.quit()
