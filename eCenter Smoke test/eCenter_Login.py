from selenium import webdriver
import time
import eCenter_buttons
from eCenter_buttons import xpaths





baseurl = "http://www.sagetimeslipsecenter.com"
username = "jknox2"
password = "password"
open_DB_button = eCenter_buttons.xpaths['Open_DB_Btn']





def eCenterLogin(pUsername, pPassword):
    #Browsing to the Website and maximizing the browser window
    eCenter_buttons.mydriver.get(baseurl)
    eCenter_buttons.mydriver.maximize_window()

    #Clear Username TextBox if already allowed "Remember Me"
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Lgn_UserField']).clear()

    #Write Username in Username TextBox
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Lgn_UserField']).send_keys(pUsername)

    #Clear Password TextBox if already allowed "Remember Me"
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Lgn_PassField']).clear()

    #Write Password in password TextBox
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Lgn_PassField']).send_keys(pPassword)

    #Click Login button
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Lgn_submitButton']).click()



def checkForDB(pUser):
    if open_DB_button == open_DB_button:
        eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Assign_user_combo']).send_keys(pUser)
        eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Open_DB_Btn']).click()




def eCenterlogout():
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Logout_Btn']).click()