from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime, time


browser = webdriver.Firefox(executable_path=r'D:\AnhTo\Setup\Wed_driver\geckodriver.exe')
browser.get('http://vccb.lge.com:8080/cb/tracker/6065708?view_id=-2')

username = browser.find_element_by_id("user")
username.send_keys("*******")

pas = browser.find_element_by_id("password")
pas.send_keys("*******")

btnLogin = browser.find_element_by_css_selector(".login_button")
btnLogin.click()

time.sleep(7000)

btnMenu = browser.find_element_by_css_selector(".bd ul.first-of-type a.displayTitleWrapper")
btnMenu.click()

btnGoToExportMenu = browser.find_element_by_id("ui-id-5")
btnGoToExportMenu.click()

btnExportToExcelTab = browser.find_element_by_id("excelExportTabPane-tab")
btnExportToExcelTab.click()

radioRoundTripSelected = browser.find_element_by_id("roundtripExcelExport")
radioRoundTripSelected.click()

btbExport = browser.find_element_by_css_selector(".actionBar input.button")
