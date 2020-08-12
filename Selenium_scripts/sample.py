# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time 


driver = webdriver.Firefox()

success = True
wd = driver

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://investor.vanguard.com/")
    wd.find_element_by_id("_cbdSearchBox").click()
    wd.find_element_by_id("_cbdSearchBox").clear()
    wd.find_element_by_id("_cbdSearchBox").send_keys("vwehx")
    wd.find_element_by_id("_cbdSearchButton").click()
    wd.find_element_by_xpath("//a[@id='profileForm:vanguardFundTabBox_tabBoxItemLink1']//span[.=' Price & Performance']").click()
    wd.find_element_by_xpath("//a[@id='profileForm:vanguardFundTabBox_tabBoxItemLink2']//span[.=' Portfolio & Management']").click()
    wd.find_element_by_xpath("//a[@id='profileForm:vanguardFundTabBox_tabBoxItemLink3']//span[.=' Fees & Minimums']").click()
    wd.find_element_by_link_text("Distributions").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
