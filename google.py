from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import *
import time

driver = webdriver.Firefox(executable_path='geckodriver/geckodriver.exe')
timeout = 60


driver.get('https://stackoverflow.com/questions/39143115/how-to-get-all-tr-elements-from-table-using-selenium')
WebDriverWait(driver, timeout)
time.sleep(2)

# fillIn = driver.find_element_by_xpath('//*[@id="seeMoreDetailsLink"]')
# fillIn.click()
#
# WebDriverWait(driver, timeout)
# time.sleep(2)

# getDetails = driver.find_element_by_css_selector('span.a-color-base:nth-child(2)')
# print(getDetails.text)

# getPrice = driver.find_element_by_id('comparison_price_row')
# print(getPrice.text)

table = driver.find_element_by_css_selector('pre.default:nth-child(6)')
print(table.text)

driver.quit()
