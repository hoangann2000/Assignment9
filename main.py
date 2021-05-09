from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(executable_path='geckodriver/geckodriver.exe')

# access
driver.get()