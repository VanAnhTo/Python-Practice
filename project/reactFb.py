from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'E:\Program\Firefox\geckodriver.exe')
browser.get('https://facebook.com/')

email = browser.find_element_by_id("email")
email.send_keys("anhanh29bg@gmail.com")

pas = browser.find_element_by_id("pass")
pas.send_keys("**************")

btnLogin = browser.find_element_by_id("loginbutton")
btnLogin.click()