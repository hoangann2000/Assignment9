from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(executable_path='geckodriver/geckodriver.exe')
timeout = 60

# 1 open driver
driver.get('http://practice.automationtesting.in/')
WebDriverWait(driver, timeout)
# 2 set max window size
driver.maximize_window()
# 3 set window size
driver.set_window_size(300,500)
# 4 get page title
print(driver.title)
# 5 print current url
print(driver.current_url)
# 6 print page source
print(driver.page_source)
time.sleep(3)
driver.quit()
