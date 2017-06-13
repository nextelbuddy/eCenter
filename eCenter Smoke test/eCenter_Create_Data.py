from selenium import webdriver
import time
import eCenter_buttons
from eCenter_buttons import xpaths
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

End_Spelling_Button = eCenter_buttons.xpaths['End_Spell_Btn']

def check_exists_by_xpath(xpath):
    try:
        eCenter_buttons.mydriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True





def Check_for_Spellcheck():
    if End_Spelling_Button == End_Spelling_Button:
        eCenter_buttons.mydriver.find_element_by_xpath(xpaths['End_Spell_Btn']).click()



def Create_baseslip(pClientName, pReferenceName, pExtra, pDescription, pDate):
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Client_Combo']).send_keys(pClientName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Ref_Combo']).send_keys(pReferenceName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Extra_Field']).send_keys(pExtra)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).clear()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).send_keys(pDescription)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).clear()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).send_keys(pDate)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Complete_box']).click()


def Create_TimeSlip(pClientName, pActivityName, pReferenceName, pExtra, pDescription, pDate, pTimeSpent):
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Menu_NewTS']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Client_Combo']).send_keys(pClientName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Task_Combo']).send_keys(pActivityName)
    eCenter_buttons.mydriver.implicitly_wait(1)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Ref_Combo']).send_keys(pReferenceName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Extra_Field']).send_keys(pExtra)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).clear()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).send_keys(pDescription)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).clear()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).send_keys(pDate)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Time_Spent']).clear()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Time_Spent']).send_keys(pTimeSpent)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Complete_box']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Slp_Submit_btn']).click()
    Check_for_Spellcheck()


def Create_ExpenseSlip(pClientName, pActivityName, pReferenceName, pExtra, pDescription, pDate):
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Menu_NewES']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Client_Combo']).send_keys(pClientName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Expense_Combo']).send_keys(pActivityName)
    eCenter_buttons.mydriver.implicitly_wait(1)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Ref_Combo']).send_keys(pReferenceName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Extra_Field']).send_keys(pExtra)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).clear()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).send_keys(pDescription)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).clear()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).send_keys(pDate)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Complete_box']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Slp_Submit_btn']).click()
    Check_for_Spellcheck()











    """
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Client_Combo']).send_keys(pClientName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Task_Combo']).send_keys(pTaskName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Ref_Combo']).send_keys(pReferenceName)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Extra_Field']).send_keys(pExtra)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Desc_Field']).send_keys(pDescription)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Date_Field']).send_keys(pDate)
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Complete_box']).click()
    eCenter_buttons.mydriver.find_element_by_xpath(xpaths['Slp_Submit_btn']).click()"""



#very slow but accurate method to build combo box list
def client_combo_select(name):
    select = eCenter_buttons.mydriver.find_element_by_id('clientCombo')
    for option in select.find_elements_by_tag_name('option'):
        if option.text == (name):
            option.click()
            break









#def Create_Client():



#def Create_Task():



#def Create_Expense():




#def Create_Reference():