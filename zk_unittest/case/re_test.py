
import sys,time,unittest
sys.path.append('F:\\zk_unittest')
from method.get_url import Get_url
from method.comm import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import re

driver = webdriver.Chrome()
driver.get('http://192.168.1.146:3000')
Login_success(driver)
driver.get('http://192.168.1.146:3000/?v=client')
time.sleep(2)
driver.find_element_by_xpath('//*[ @id="mgr-s"and @class="mgr-a"]' ).click()
time.sleep(10)