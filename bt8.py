from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(executable_path='geckodriver/geckodriver.exe')
timeout = 60

# 1 open driver
driver.get('http://practice.automationtesting.in/')
WebDriverWait(driver, timeout)
time.sleep(2)

# click my account
driver.find_element_by_id('menu-item-50').click()
WebDriverWait(driver, timeout)
time.sleep(2)

# fill in my data
# driver.find_element_by_id('username').send_keys('hhhahahaha@gmail.com')
# driver.find_element_by_id('password').send_keys('sffwrv54ASDFAFGDS333')
# fill in assignment data
driver.find_element_by_id('username').send_keys('tomsmith')
driver.find_element_by_id('password').send_keys('SuperSecretPassword!')


# click register
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]').click()
WebDriverWait(driver, timeout)
time.sleep(3)

# print page title
print(driver.title)

time.sleep(10)
driver.quit()



