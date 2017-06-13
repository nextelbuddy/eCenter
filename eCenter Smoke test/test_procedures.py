# -*- coding: utf-8 -*-
from selenium import webdriver
import eCenter_buttons
import eCenter_Login
import eCenter_Create_Data
import time
from eCenter_buttons import xpaths
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

#--------------------------------------------------------------------------------------------------------------------------------------------------------#

End_Spelling_Button = eCenter_buttons.xpaths['End_Spell_Btn']

def Check_for_Spellcheck():
    if End_Spelling_Button == End_Spelling_Button:
        eCenter_buttons.mydriver.find_element_by_xpath(xpaths['End_Spell_Btn']).click()


def Create_TimeSlip(pClientName, pActivityName, pReferenceName):
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Menu_NewTS']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Client_Combo']).send_keys(pClientName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Task_Combo']).send_keys(pActivityName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Ref_Combo']).send_keys(pReferenceName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Complete_box']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Slp_Submit_btn']).click()



#def Client_combo_lists(x):
    #clients = Select(eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Client_Combo'])).options
    #for index, value in enumerate(clients, 1):
        #break


eCenter_Login.eCenterLogin('jknox2', 'password')

eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Menu_NewTS']).click()

clients = Select(eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Client_Combo'])).options


test = False


#need to store client list in memory after it is indexed the first time otherwise the list will be lost when we go back to the page
#python create dynamic list (search parameter in google)

for client in clients:
    print ((client.text))
    if not test:
        test = True
    else:
        eCenter_Create_Data.Create_TimeSlip(client.text, 'bid', 'aaa-project', 'DTU Extra TIME', 'This is a test for the DTU Smoketest Timeslips', '04/1/2017', '01:02:03')




#Create_TimeSlip(clients[i], 'BID', 'aaa-project')










##Create_baseslip(pClientName, pReferenceName, pExtra, pDescription, pDate)
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Extra_Field']).send_keys(pExtra)
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).clear()
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).send_keys(pDescription)
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).clear()
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).send_keys(pDate)
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Time_Spent']).clear()
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Time_Spent']).send_keys(pTimeSpent)
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Complete_box']).click()
#eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Slp_Submit_btn']).click()
