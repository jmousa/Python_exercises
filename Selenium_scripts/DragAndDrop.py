# -*- coding: utf-8 -*-
#================================================================
#from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC 
#================================================================

from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


import time

driver = webdriver.Chrome


success = True
wd = driver()
wd.implicitly_wait(5)


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
#===============================================================
#	Read input file
#==============================================================
	
fh = open ("Data_Input.txt", "r")


content = fh.readlines()

Dirty_user_name = content[0]
user_name = Dirty_user_name [:-1]

Dirty_password = content[1]
password = Dirty_password[:-1]


url = content[2]

	
fh.close()

try:
#==========================================================
#   Connect to the website and Login
#==========================================================
    wd.get(url)
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").clear
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").send_keys(user_name)
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").send_keys(password)
    time.sleep(1)
    wd.find_element_by_id("formLoginSubmit").click()
    time.sleep(1)
    alert = wd.switch_to_alert()
    time.sleep(2)
    alert.accept()
    time.sleep(2)
    wd.find_element_by_class_name("auditor").click()
    time.sleep(2)
    
#==========================================================
#   Select a site and a room
#==========================================================

    wd.find_element_by_id("selectTypeSite").click()
    time.sleep(5)
    wd.find_element_by_name("formFilterListSite").click()
    time.sleep(2)
    el = wd.find_element_by_id('formFilterListSite')
    for option in el.find_elements_by_tag_name('option'):
        if option.text == 'RTP':
            option.click() # select() in earlier versions of webdriver
            break
    time.sleep(3)
    wd.find_element_by_id("aFL").click()
    time.sleep(2)
    alert = wd.switch_to_alert()
    time.sleep(2)
    alert.accept()
    time.sleep(2)
    
#==========================================================
#   Audit the tile
#==========================================================

    time.sleep(2)
    wd.find_element_by_id("generalRack2876").click()
    time.sleep(2)

    
#=============================================================
#   Drag and Drop
#=============================================================

    

    wd.find_element_by_id("fourteen").click()
    time.sleep(1)
    source_element = wd.find_element_by_id('fourteen')
    time.sleep(1)
    dest_element = wd.find_element_by_id('binContainer')
    time.sleep(1)
    from selenium.webdriver import ActionChains
    time.sleep(1)
    action_chains = ActionChains(wd)
    time.sleep(1)
    ActionChains(wd).drag_and_drop(source_element, dest_element).perform()
    time.sleep(1)
    
    
    wd.find_element_by_id("twelve").click()
    time.sleep(1)
    source_element = wd.find_element_by_id('twelve')
    time.sleep(1)
    dest_element = wd.find_element_by_id('binContainer')
    time.sleep(1)
    from selenium.webdriver import ActionChains
    time.sleep(1)
    action_chains = ActionChains(wd)
    time.sleep(1)
    ActionChains(wd).drag_and_drop(source_element, dest_element).perform()
    time.sleep(2)

#	Take a screen shot
    wd.save_screenshot("C:\\Users\\mousaj\\Desktop\\mobile-capture-testing\\Results\\Drag_And_Drop_screenShot.png")

    
    #wd.find_element_by_id("binContainer").click()
    #source_element = wd.find_element_by_id('binContainer')
    #time.sleep(1)
    #dest_element = wd.find_element_by_id('fourteen')
    #time.sleep(1)
    #from selenium.webdriver import ActionChains
    #time.sleep(1)
    #action_chains = ActionChains(wd)
    #time.sleep(1)
    #ActionChains(wd).drag_and_drop(source_element, dest_element).perform()
    #time.sleep(1)
   

#=============================================================
#   Select the audit checkbox
#=============================================================

    wd.find_element_by_class_name("entypo-check").click()
    time.sleep(2)


    
    #wd.find_element_by_id("launchSync").click()
    #time.sleep(2)


    #alert = wd.switch_to_alert()
    #time.sleep(2)
    #alert.accept()
    #time.sleep(2)


#==========================================================
#   Logout
#==========================================================

    wd.find_element_by_id("logout").click()
    time.sleep(2)
    
#==========================================================
#   Write the script run result to the log file
#==========================================================

    FH = open("C:\\Users\\mousaj\\Desktop\\mobile-capture-testing\\Results\Automation_Log_File.txt","a")	    
    FH.write("Audit_A_Tile_DRAG_AND_DROP script ran successfully.\n")
    FH.close 

    
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
