from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

path = './chromedriver'  # introduce path here

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)