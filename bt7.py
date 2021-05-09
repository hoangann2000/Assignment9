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

# fill in
driver.find_element_by_id('reg_email').send_keys('hhhahahaha@gmail.com')
driver.find_element_by_id('reg_password').send_keys('sffwrv54ASDFAFGDS333')

# click register
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]').click()

WebDriverWait(driver, timeout)
# time.sleep(10)
# driver.quit()



