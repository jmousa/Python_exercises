# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#from sys import argv
#script, country = argv

success = True
wd = WebDriver()
wd.implicitly_wait(2)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://en.wikipedia.org/wiki/Main_Page")
    wd.find_element_by_id("searchInput").click()
    wd.find_element_by_id("searchInput").clear()
    wd.find_element_by_id("searchInput").send_keys("madagascar")
    wd.find_element_by_id("searchButton").click()
    if not ("Malagasy" in wd.find_element_by_css_selector("a[title=\"Malagasy people\"]").txt):
        success = False
        print("verifyTextPresent failed")
    print("Malagasy")
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
