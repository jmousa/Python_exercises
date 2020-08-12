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
    wd.get("https://investor.vanguard.com/corporate-portal/")
    wd.find_element_by_css_selector("span.linkStyle").click()
    wd.find_element_by_link_text("Open an IRA in minutes").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
