from selenium import webdriver
import time
import eCenter_buttons
from eCenter_buttons import xpaths
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys









baseurl = "http://www.sagetimeslipsecenter.com"
username = "jknox1"
password = "password"



eCenter_buttons.mydriver.get(baseurl)
eCenter_buttons.mydriver.maximize_window()



#Clear Username TextBox if already allowed "Remember Me"
eCenter_buttons.ClearField('Lgn_UserField')

#Write Username in Username TextBox
eCenter_buttons.ClickButton('Lgn_UserField').send_keys(username)


#Clear Password TextBox if already allowed "Remember Me"
eCenter_buttons.ClearField('Lgn_PassField')

#Write Password in password TextBox
eCenter_buttons.ClickButton('Lgn_PassField').send_keys(password)


#Click Login button

eCenter_buttons.ClickButton('Lgn_submitButton')


#Click Admin Functions button
eCenter_buttons.ClickButton('Menu_AdminFunc')




nameSelectID = eCenter_buttons.mydriver.find_element_by_id('phContent_addNames_ddlNames')

def Create_Task():
    nameSelect = Select(nameSelectID)
    nameSelect.select_by_value('task')
    eCenter_buttons.mydriver.implicitly_wait(2)

    #ECBtns.GetBtn('bNewName').click()

    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Button_NewName']).click()
    eCenter_buttons.mydriver.implicitly_wait(2)
    eCenter_buttons.mydriver.find_element_by_xpath ('//*[@id="phContent_NewTask1_txtNickname1"]').click()
    eCenter_buttons.mydriver.find_element_by_xpath ('//*[@id="phContent_NewTask1_txtNickname1"]').send_keys('eCenter Smoke Test 1')
    eCenter_buttons.mydriver.find_element_by_xpath ('//*[@id="phContent_NewTask1_txtNickname2"]').send_keys('eCenter Smoke Test 2')
    eCenter_buttons.mydriver.find_element_by_xpath ('//*[@id="phContent_NewTask1_txtNickname1"]').send_keys(Keys.TAB)




Create_Task()

