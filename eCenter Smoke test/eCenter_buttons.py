from selenium import webdriver


mydriver = webdriver.Chrome('C:\Python34\selenium\webdriver\chrome\chromedriver.exe')



    #lint:disable
xpaths = { 'Lgn_UserField'     : "//*[@id='ContentPlaceHolder1_logLogin_UserName']",
           'Lgn_PassField'     : "//*[@id='ContentPlaceHolder1_logLogin_Password']",
           'Lgn_submitButton'  : "//*[@id='ContentPlaceHolder1_logLogin_Login']",
           'Menu_NewTS'        : '//*[@id="LeftNav1_menuLevelOneRepeater_menuLevelTwoRepeater_0_HyperLink1_0"]',
           'Menu_NewES'        : '//*[@id="LeftNav1_menuLevelOneRepeater_menuLevelTwoRepeater_0_HyperLink1_1"]',
           'Menu_AdminFunc'    : '//*[@id="LeftNav1_menuLevelOneRepeater_firstLevelAnchor_5"]',
           'Button_NewName'    : '//*[@id="phContent_addNames_btnAddName"]',
           'Slp_Radio_Btn'     : '//*[@id="phContent_rptSlips_rdoRow_0"]',
           'Duplicate_Btn'     : '//*[@id="phContent_rptSlips_lnkDuplicateSlip_0"]',
           'Slp_Submit_btn'    : '//*[@id="saveTimeSlip"]',
           'Slip_List_Btn'     : '//*[@id="LeftNav1_menuLevelOneRepeater_firstLevelAnchor_0"]',
           'Open_DB_Btn'       : '//*[@id="phContent_btnSelectUser"]',
           'Assign_user_combo' : '//*[@id="phContent_ddlUsers"]',
           'Client_Combo'      : '//*[@id="clientCombo"]',
           'Task_Combo'        : '//*[@id="taskCombo"]',
           'Expense_Combo'     : '//*[@id="expenseCombo"]',
           'Ref_Combo'         : '//*[@id="refCombo"]',
           'Extra_Field'       : '//*[@id="contentMain"]/div[2]/div[2]/div/table/tbody/tr[5]/td[2]/div/div/input',
           'Desc_Field'        : '//*[@id="tsDescEdit"]',
           'Date_Field'        : '//*[@id="fDateEdit"]',
           'Time_Spent'        : '//*[@id="timeSpentEdit"]',
           'Complete_box'      : '//*[@id="chkComplete"]',
           'End_Spell_Btn'     : '//*[@id="endSpelling"]',
           'Logout_Btn'        : '//*[@id="GlobalNav1_lnkLogout"]',
}
    #lint:enable



#def GetBtn(pName):element
#  = eCenter_buttons.mydriver.find_element_by_xpath(xpaths[pName])

def ClickButton(pName):
    mydriver.find_element_by_xpath(xpaths[pName]).click()

def ClearField(pName):
    mydriver.find_element_by_xpath(xpaths[pName]).clear()
