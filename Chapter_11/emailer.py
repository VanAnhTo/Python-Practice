import requests,bs4, sys, re, time
from selenium import webdriver
'''
email = sys.argv[1]
print('Dia chi email: '+ email)

emailContent = ' '.join(sys.argv[2:])
print('Day la noi dung email: '+ emailContent )
'''
browser = webdriver.Firefox()
browser.get('https://mail.google.com')
time.sleep(3)

username = browser.find_element_by_id('identifierId')
username.send_keys('anhanh29bg')

nextBtn = browser.find_element_by_id('identifierNext')
nextBtn.click()
time.sleep(3)

password = browser.find_element_by_name('password')
password.send_keys('Giodongthoi#12')

nextBtn = browser.find_element_by_id('passwordNext')
nextBtn.click()
time.sleep(7)

newEmailBtn = browser.find_element_by_class_name('T-I.J-J5-Ji.T-I-KE.L3')
newEmailBtn.click()

recipient = browser.find_element_by_name('to')
recipient.send_keys('Vananhto.bg@gmail.com')

mailSubject = browser.find_element_by_name('subjectbox')
mailSubject.send_keys('Test email')

mailContent = browser.find_element_by_css_selector('div.Ar.Au div.Am.Al.editable.LW-avf')
mailContent.send_keys('This is content of test email, it is sent automatically. \n\n Do not reply this email')

sentBtn = browser.find_element_by_css_selector('div div.T-I.J-J5-Ji.aoO.T-I-atl.L3')
sentBtn.click()