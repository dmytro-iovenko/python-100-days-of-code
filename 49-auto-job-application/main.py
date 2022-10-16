from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = YOUR_LOGIN_EMAIL
ACCOUNT_PASSWORD = YOUR_LOGIN_PASSWORD

chrome_driver_path = "C:/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Cincinnati%2C%20Ohio%2C%20United%20States&geoId=106310628&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)