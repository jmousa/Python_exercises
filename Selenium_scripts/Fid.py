# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://www.fidelity.com/")
    wd.find_element_by_css_selector("img[alt=\"CUSTOMER LOGIN\"]").click()
    wd.find_element_by_id("userId-input").click()
    wd.find_element_by_id("userId-input").clear()
    wd.find_element_by_id("userId-input").send_keys("Suzaka144")
    wd.find_element_by_id("password").click()
    wd.find_element_by_id("password").clear()
    wd.find_element_by_id("password").send_keys("Nebaka231")
    wd.find_element_by_id("fs-login-button").click()
    wd.find_element_by_xpath("//div[@class='account-selector--accounts-wrapper']/div[3]").click()
    wd.find_element_by_id("tab-2").click()
    wd.find_element_by_id("tab-3").click()
    wd.find_element_by_id("tab-4").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
