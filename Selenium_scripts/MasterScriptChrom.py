# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os
import time
import datetime


WebDriver = webdriver.Chrome


#=======================================================================
# Creating BD Tool Result directory
#=======================================================================
        

#ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H')
#ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M')
ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')


if not os.path.exists ("C:\\Users\\Public\\Some_file"):
    os.makedirs ("C:\\Users\\Public\\Chrome_BU_Results" + " " + ts)
    
    
path = ("C:\\Users\\Public\\Chrome_BU_Results" + " " + ts)

#=======================================================================
# Open the log file for writing 
#=======================================================================
        
FH = open(path+"/Log_File.txt","a")
FH.write("Log file created successfully.\n\n")

#=======================================================================


fh = open ("C:\\Users\\Public\\BD_Data_Input.txt", "r")

content = fh.readlines()

url = content[0]

Dirty_user_name = content[1]
viewer = Dirty_user_name [:-1]
Dirty_password = content[2]
password1 = Dirty_password[:-1]

Dirty_user_name = content[3]
disputer = Dirty_user_name [:-1]
Dirty_password = content[4]
password2 = Dirty_password[:-1]

Dirty_user_name = content[5]
moderator = Dirty_user_name [:-1]
Dirty_password = content[6]
password3 = Dirty_password[:-1]

Dirty_user_name = content[7]
rejector = Dirty_user_name [:-1]
Dirty_password = content[8]
password4 = Dirty_password[:-1]


Dirty_user_name = content[9]
acceptor = Dirty_user_name [:-1]

password5 = content[10]



#fh.close()

FH.write("Credential file opend successfully\n\n")

#=======================================================================
#Reseting data
#=======================================================================

import urllib.request

result = urllib.request.urlopen("http://10.110.53.62/api/reset").read()

#print (result)

if result == b"OK":
    FH.write("Data has been reset correctly in the Database\n\n")
else:
    FH.write("There was an error resetting the data\n")
    

success = True
wd = WebDriver()
wd.implicitly_wait(35)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

#=======================================================================
# Starting the tile view script
#=======================================================================
try:
    FH.write("Starting the view a tile script\n\n")
    FH.write("Connecting to the website\n\n")
    wd.get(url)
    if not ("Login with LDAP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to connect to the website. Check your URL")
        raise Exception()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").send_keys(viewer)
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").send_keys(password1)
    time.sleep(1)
    wd.find_element_by_id("formLoginSubmit").click()
    time.sleep(1)
    if not ("Site" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to log in. Check your User name and/or password\n")
        raise Exception()
    wd.refresh()
    time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[1]//option[6]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[1]//option[6]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']//select[.='Select a room...Er6Er8Er10']//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']//select[.='Select a room...Er6Er8Er10']//option[2]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[3]//option[15]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[3]//option[15]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[4]//option[11]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[4]//option[11]").click()
        time.sleep(2)
    if not ("Height:" in wd.find_element_by_tag_name("html").text):
        success = False

#=======================================================================
#Writing test result to log file
#=======================================================================

    if success:
        FH.write("VIEW A TILE TEST PASSED: Tile details displayed successfully\n\n")
        
#=======================================================================

        
# Taking screen shot and writing result to BD_Results directory

    wd.get_screenshot_as_file(path+"/Regular Viewer.png")
    #FH.write("screen shot taken successfully\n")

#=======================================================================           
# Logging out
#=======================================================================
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuLogout").click()
        
    
#=======================================================================
# Starting the Dispute tool script
#=======================================================================

    FH.write("Starting the Disput a tile script\n\n")
    wd.get(url)
    time.sleep(1)
    if not ("Login with LDAP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to connect to website, check your URL\n")
    wd.find_element_by_id("formLoginUser").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").send_keys(disputer)
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").send_keys(password2)
    time.sleep(1)
    wd.find_element_by_id("formLoginSubmit").click()
    time.sleep(1)
    if not ("Site" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to log in. Check your User name and/or password\n")
    wd.refresh()
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[1]//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[1]//option[2]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[2]//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[2]//option[2]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[3]//option[7]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[3]//option[7]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[4]//option[12]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[4]//option[12]").click()
        time.sleep(3)
    if not ("Height:" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to pull up the tile for dispute. \n")
    wd.find_element_by_id("add-dispute").click()
    if not ("DCOE" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to add DCOE Tile to list of dispute tile \n")
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[1]//option[3]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[1]//option[3]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[2]//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[2]//option[2]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']//select[.='Select a row...123']//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']//select[.='Select a row...123']//option[2]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[4]//option[14]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[4]//option[14]").click()
        time.sleep(3)
    if not ("Height:" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to pull up the tile. \n")
    wd.find_element_by_id("add-dispute").click()
    if not ("RTP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to add RTP Tile to list of dispute tile \n")
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[1]//option[7]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[1]//option[7]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']//select[.='Select a room...HDLLab']//option[2]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']//select[.='Select a room...HDLLab']//option[2]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[3]//option[58]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[3]//option[58]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[4]//option[76]").is_selected():
        wd.find_element_by_xpath("//div[@class='demo']/form/fieldset/select[4]//option[76]").click()
        time.sleep(3)
    wd.find_element_by_id("tile").click()
    time.sleep(1)
    wd.find_element_by_id("add-dispute").click()
    time.sleep(1)
    wd.find_element_by_css_selector("input[type=\"search\"]").click()
    time.sleep(1)
    wd.find_element_by_css_selector("input[type=\"search\"]").clear()
    time.sleep(1)
    wd.find_element_by_css_selector("input[type=\"search\"]").send_keys("DC")
    time.sleep(1)
    if not ("DCOE" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("The search functionality failed. \n")
    wd.find_element_by_css_selector("input[type=\"search\"]").click()
    time.sleep(1)
    wd.find_element_by_css_selector("input[type=\"search\"]").clear()
    time.sleep(1)
    wd.find_element_by_css_selector("input[type=\"search\"]").send_keys("RTP")
    time.sleep(1)
    if not ("RTP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("The search functionality failed. \n")
    wd.find_element_by_css_selector("input[type=\"search\"]").click()
    time.sleep(1)
    wd.find_element_by_css_selector("input[type=\"search\"]").clear()
    time.sleep(1)
    wd.find_element_by_css_selector("input[type=\"search\"]").send_keys("171")
    time.sleep(1)
    if not ("171" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("The search functionality failed. \n")
    wd.refresh()
    wd.find_element_by_xpath("//table[@id='viewDisputeTable']//td[.='Lab1']").click()
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-comment").click()
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-comment").click()
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-comment").clear()
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-comment").send_keys("please assign to others")
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-updateComment").click()
    time.sleep(1)
    if not ("please assign to others" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Application failed to add a comment. \n")
    wd.find_element_by_xpath("//tr[@class='even']//td[.='Lab6']").click()
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-comment").click()
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-comment").clear()
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-comment").send_keys("Please give me this tile")
    time.sleep(1)
    wd.find_element_by_id("viewDisputeTable-updateComment").click()
    time.sleep(1)
    if not ("Please give me this tile" in wd.find_element_by_tag_name("html").text):
        FH.write("Application failed to add a comment. \n")
    wd.find_element_by_xpath("//table[@id='viewDisputeTable']//td[.='HDLLab']").click()
    time.sleep(1)
    wd.find_element_by_xpath("//table[@id='viewDisputeTable']/tbody/tr[3]/td[1]/button").click()
    time.sleep(1)
    wd.get_screenshot_as_file(path+"/Disput_Tile.png")
    time.sleep(1)
    wd.find_element_by_id("dispute-btn").click()
    #time.sleep(30)
    #alert = wd.switch_to_alert()
    #time.sleep(1)
    #alert.accept()
    #time.sleep(1)
    try:
        WebDriverWait(wd,60).until(EC.alert_is_present())
        alert = wd.switch_to_alert()
        time.sleep(1)
        alert.accept()
        #print ("alert accepted")
		
    except TimeoutException:
        print ("No Allert")
    
#=======================================================================
#    Writing Test results to the log file
#=======================================================================
    
    if not ("No data available in table" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Dipsute failed to post \n")
    if success:
        FH.write("DISPUTE A TILE TEST PASSED: 2 tiles were posted successfully\n\n")

#=======================================================================
#   Logging out
#=======================================================================
    
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuLogout").click()
    
#=======================================================================
# Starting the Moderate Script
#=======================================================================

    FH.write("Starting the moderate a tile script\n\n")
    wd.get(url)
    time.sleep(1)
    if not ("Login with LDAP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to connect to Website. Check your URL \n")
        raise Exception()
    wd.find_element_by_id("formLoginUser").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").send_keys(moderator)
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").send_keys(password3)
    time.sleep(1)
    wd.find_element_by_id("formLoginSubmit").click()
    time.sleep(1)
    if not ("Site" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to log in. Check your User name and/or password\n")
        raise Exception()

#=======================================================================
# Taking screen shot and writing result to BD_Results directory
#=======================================================================

    wd.get_screenshot_as_file(path+"/Moderate_Tile.png")
    
#=======================================================================
    if not (len(wd.find_elements_by_css_selector("div.pushIcon")) != 0):
        success = False
        FH.write("MODERATE A TILE FAILED: Please reset the data\n\n")
    if not (len(wd.find_elements_by_css_selector("div.pullIcon")) != 0):
        success = False
        FH.write("MODERATE A TILE FAILED: Please reset the data\n\n")
    wd.find_element_by_xpath("//table[@id='viewModerateTable']//td[.='CTD / VNX']").click()
    time.sleep(1)
    if not wd.find_element_by_css_selector("input.tableCheck").is_selected():
        wd.find_element_by_css_selector("input.tableCheck").click()
        time.sleep(1)
    #wd.find_element_by_id("viewModerateTable-comment").click()
    #time.sleep(1)
    wd.find_element_by_id("viewModerateTable-comment").click()
    time.sleep(1)
    wd.find_element_by_id("viewModerateTable-comment").clear()
    time.sleep(1)
    wd.find_element_by_id("viewModerateTable-comment").send_keys("Ok, I will do that")
    time.sleep(1)
    wd.find_element_by_id("viewModerateTable-updateComment").click()
    time.sleep(1)
    wd.find_element_by_xpath("//tr[@class='even']//td[.='Rubicon / Beatle']").click()
    time.sleep(1)
    if not wd.find_element_by_css_selector("tr.even.selected > td.sorting_1 > input.tableCheck").is_selected():
        wd.find_element_by_css_selector("tr.even.selected > td.sorting_1 > input.tableCheck").click()
    wd.find_element_by_id("viewModerateTable-comment").click()
    time.sleep(1)
    wd.find_element_by_id("viewModerateTable-comment").clear()
    time.sleep(1)
    wd.find_element_by_id("viewModerateTable-comment").send_keys("OK, I will do that")
    time.sleep(1)
    wd.find_element_by_id("viewModerateTable-updateComment").click()
    time.sleep(1)
    wd.find_element_by_css_selector("div[title=\"Ok, I will do that\"]").click()
    time.sleep(1)
    if not wd.find_element_by_xpath("//div[@id='ownerSelect']/form/fieldset/select//option[20]").is_selected():
        wd.find_element_by_xpath("//div[@id='ownerSelect']/form/fieldset/select//option[20]").click()
        time.sleep(1)
    wd.find_element_by_xpath("//tr[@class='even']//td[.='1']").click()
    time.sleep(1)
    if not wd.find_element_by_xpath("//div[@id='ownerSelect']/form/fieldset/select//option[58]").is_selected():
        wd.find_element_by_xpath("//div[@id='ownerSelect']/form/fieldset/select//option[58]").click()
        time.sleep(1)
    wd.find_element_by_id("btnModerate").click()
    #time.sleep(30)
    #alert = wd.switch_to_alert()
    #time.sleep(1)
    #alert.accept()
    #time.sleep(1)
    
    try:
        WebDriverWait(wd,60).until(EC.alert_is_present())
        alert = wd.switch_to_alert()
        time.sleep(1)
        alert.accept()
        #print ("alert accepted")
		
    except TimeoutException:
        print ("No Allert")
    
    FH.write("MODERTE A TILE TEST PASSED: 2 tiles were moderated successfully\n\n")
    
#======================================================================
# Logging out
#=======================================================================
    
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuLogout").click()

    
#=======================================================================
# Starting the Reject a tile script
#=======================================================================
    
    FH.write("Starting the Reject a tile script\n\n")
    wd.get(url)
    time.sleep(1)
    if not ("Login with LDAP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to connect to the web Site. Chech the URL")
    wd.find_element_by_id("formLoginUser").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").send_keys(rejector)
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").send_keys(password4)
    time.sleep(1)
    wd.find_element_by_id("formLoginSubmit").click()
    time.sleep(1)
    if not ("Site" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to log in. Check your User name and/or password\n")
        raise Exception()
        time.sleep(1)
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuApproval").click()
    time.sleep(1)
    if not ("DCOE" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("TEST FAILED: No Tile available to accept or reject\n\n")
        time.sleep(1)
    if not wd.find_element_by_css_selector("input.tableCheck").is_selected():
        wd.find_element_by_css_selector("input.tableCheck").click()
        time.sleep(1)
    wd.find_element_by_xpath("//table[@id='viewAJTable']//td[.='CTD / VNX']").click()
    time.sleep(1)
    wd.find_element_by_id("viewAJTable-comment").click()
    time.sleep(1)
    wd.find_element_by_id("viewAJTable-comment").clear()
    time.sleep(1)
    wd.find_element_by_id("viewAJTable-comment").send_keys("No I do not want this tile")
    time.sleep(1)
    wd.find_element_by_id("viewAJTable-updateComment").click()
    time.sleep(1)
    wd.find_element_by_id("rejectTile").click()
    #time.sleep(30)
    #alert = wd.switch_to_alert()
    #time.sleep(1)
    #alert.accept()
    time.sleep(2)
    
    try:
        WebDriverWait(wd,60).until(EC.alert_is_present())
        alert = wd.switch_to_alert()
        time.sleep(1)
        alert.accept()
        #print ("alert accepted")
        time.sleep(2)
		
    except TimeoutException:
        print ("No Allert")
      
    if not ("No data available in table" in wd.find_element_by_tag_name("html").text):
        success = False
        print("REJECT A TILE TEST FAILED")
        
    wd.get_screenshot_as_file(path+"/Reject_tile.png")
        
#=======================================================================
#Writing test result to log file
#=======================================================================
    
    if success:
        FH.write("REJECT A TILE TEST PASSED: One tile was rejected\n\n")

#=======================================================================
# Logging out
#=======================================================================
    
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuLogout").click()
  
  
#=======================================================================
# Starting the accept a tile script
#=======================================================================

    FH.write("Starting the Accept a tile script\n\n")
    wd.get(url)
    time.sleep(1)
    if not ("Login with LDAP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to connect to the website. Check you URL")
    wd.find_element_by_id("formLoginUser").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").send_keys(acceptor)
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").send_keys(password5)
    time.sleep(1)
    wd.find_element_by_id("formLoginSubmit").click()
    time.sleep(1)
    if not ("Site" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to log in. Check your User name and/or password\n")
        raise Exception()
        time.sleep(1)
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuApproval").click()
    time.sleep(1)
    if not ("RTP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("ACCEPT A TILE FAILED: No tile available to accept\n\n")
        time.sleep(1)
    if not wd.find_element_by_css_selector("input.tableCheck").is_selected():
        wd.find_element_by_css_selector("input.tableCheck").click()
        time.sleep(1)
    wd.find_element_by_xpath("//table[@id='viewAJTable']//td[.='Rubicon / Beatle']").click()
    time.sleep(1)
    wd.find_element_by_id("viewAJTable-comment").click()
    time.sleep(1)
    wd.find_element_by_id("viewAJTable-comment").clear()
    time.sleep(1)
    wd.find_element_by_id("viewAJTable-comment").send_keys("OK, take it away")
    time.sleep(1)
    wd.find_element_by_id("viewAJTable-updateComment").click()
    time.sleep(3)
    wd.find_element_by_id("acceptTile").click()
    #time.sleep(30)
    #alert = wd.switch_to_alert()
    #time.sleep(1)
    #alert.accept()
    #time.sleep(1)
    
    try:
        WebDriverWait(wd,60).until(EC.alert_is_present())
        alert = wd.switch_to_alert()
        time.sleep(1)
        alert.accept()
        #print ("alert accepted")
		
    except TimeoutException:
        print ("No Allert")
    
    time.sleep(3)
    if not ("No data available in table" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Either the tile was not accepted or more tiles need to be accepted\n\n")
        
    if success:  
        FH.write("ACCEPT A TILE TEST PASSED: One tile was accpeted\n\n")
        wd.get_screenshot_as_file(path+"/Accept_tile.png")
        
#=======================================================================
# Logging out
#=======================================================================
    
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuLogout").click()
    
    
#=======================================================================
# Starting the Admin script
#=======================================================================
  
  
    FH.write("Starting the admin script\n\n")
    wd.get(url)
    if not ("Login with LDAP" in wd.find_element_by_tag_name("html").text):
        success = False
        FH.write("Failed to connect to the website. Check your URL")
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginUser").clear()
    wd.find_element_by_id("formLoginUser").send_keys(moderator)
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").click()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").clear()
    time.sleep(1)
    wd.find_element_by_id("formLoginPassword").send_keys(password3)
    time.sleep(1)
    wd.find_element_by_id("formLoginSubmit").click()
    time.sleep(1)
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuUserAdmin").click()
    time.sleep(1)
    wd.find_element_by_id("newUser").click()
    time.sleep(1)
    wd.find_element_by_id("userName").click()
    time.sleep(1)
    wd.find_element_by_id("userName").clear()
    time.sleep(1)
    wd.find_element_by_id("userName").send_keys("Admin_Test")
    time.sleep(1)
    wd.find_element_by_id("userEmail").click()
    time.sleep(1)
    wd.find_element_by_id("userEmail").clear()
    time.sleep(1)
    wd.find_element_by_id("userEmail").send_keys("Admin_Test@emc.com")
    time.sleep(1)
    wd.find_element_by_id("userSave").click()
    time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='left-user-div']/select//option[1]").is_selected():
        wd.find_element_by_xpath("//div[@class='left-user-div']/select//option[1]").click()
        time.sleep(1)
    if not wd.find_element_by_xpath("//div[@class='left-list']/select/option[@value='6']").is_selected():
        wd.find_element_by_xpath("//div[@class='left-list']/select/option[@value='6']").click()
        time.sleep(1)
    wd.find_element_by_id("ownerAdd").click()
    time.sleep(1)
    wd.find_element_by_id("userSave").click()
    time.sleep(1)
    wd.get_screenshot_as_file(path+"/Admin.png")
    if not wd.find_element_by_xpath("//div[@class='left-user-div']/select//option[1]").is_selected():
        wd.find_element_by_xpath("//div[@class='left-user-div']/select//option[1]").click()
        time.sleep(1)
    wd.find_element_by_id("delUser").click()
    time.sleep(2)
    
    FH.write("ADMIN TEST PASSED: one user was added and deleted\n\n")
    time.sleep(2)  
    
#=======================================================================
# Logging out
#=======================================================================
    
    wd.find_element_by_id("headerMenu").click()
    time.sleep(1)
    wd.find_element_by_id("menuLogout").click()
    time.sleep(1)

    
finally:
    wd.quit()
    if not success:
        #FH.write("TEST FAILED: There was an error in the data\n")
        raise Exception()
