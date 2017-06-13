from selenium import webdriver
import eCenter_buttons
import eCenter_Login
import eCenter_Create_Data
import time
from eCenter_buttons import xpaths
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select





#                 Accepts 2 parameters (pUsername, pPassword)
eCenter_Login.eCenterLogin('jknox2', 'password')

#eCenter_Login.checkForDB('ShawnR')

#                  list of the parameters that the Create slips method accepts
#                 (pClientName, pActivityName, pReferenceName, pExtra, pDescription, pDate, pTimeSpent)

eCenter_Create_Data.Create_TimeSlip('Abington', 'bid', 'aaa-project', 'DTU Extra TIME', 'This is a test for the DTU Smoketest Timeslips', '04/1/2017', '01:02:03')

eCenter_Create_Data.Create_ExpenseSlip('Acton', 'Cleanup supplies', 'Acton-project01', 'DTU Extra EXP', 'This is a test for the DTU Smoketest Expense slips', '04/2/2017')

#eCenter_Login.eCenterlogout()



#eCenter_Create_Data.client_combo_select('Yarmouth  |  02664')





