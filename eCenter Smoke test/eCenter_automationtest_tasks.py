from selenium import webdriver
import eCenter_buttons
import eCenter_Login
from eCenter_buttons import xpaths


def duplicateSlips():
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Slp_Radio_Btn']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Duplicate_Btn']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Slp_Submit_btn']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Slip_List_Btn']).click()






eCenter_Login.eCenterLogin()


for x in range(1, 20):
    duplicateSlips()