from selenium import webdriver
from selenium.webdriver.support.ui import *
import time

driver = webdriver.Firefox(executable_path='geckodriver/geckodriver.exe')
timeout = 60

# 1 open driver
driver.get('https://itmscoaching.herokuapp.com/form')
WebDriverWait(driver, timeout)
time.sleep(2)

# fill in
driver.find_element_by_id('first-name').send_keys('Binh')
driver.find_element_by_id('last-name').send_keys('Nguyen')
driver.find_element_by_id('job-title').send_keys('Tester')
driver.find_element_by_id('radio-button-3').click()
driver.find_element_by_id('checkbox-2').click()
# select drop downn
Select(driver.find_element_by_id('select-menu')).select_by_visible_text('5-9')
driver.find_element_by_id('datepicker').send_keys('07/20/2011')

time.sleep(10)
# click submit
driver.find_element_by_xpath('/html/body/div[1]/form/div/div[8]/a').click()

WebDriverWait(driver, timeout)
# time.sleep(10)
# driver.quit()



