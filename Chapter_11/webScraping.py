import requests,bs4

#Downloading a Web Page with the requests.get() Function
'''
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])
'''

#Checking for Errors
'''
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
'''

#Saving Downloaded Files to the Hard Drive
'''
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
'''
#Parsing HTML with the BeautifulSoup Module

#install package: beautifulsoup4
#Creating a BeautifulSoup Object from HTML
'''
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
'''
'''
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)
'''
#Finding an Element with the select() Method

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
'''
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())
'''
#Getting Data from an Element’s Attributes

#Controlling the Browser with the selenium Module
#Starting a Selenium-Controlled Browser
#Finding Elements on the Page
'''
from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
'''
#Clicking the Page
'''
from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Cracking Codes with Python')
type(linkElem)
linkElem.click() # follows the "Read It Online" link
'''
#Filling Out and Submitting Forms
'''
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
'''

#Sending Special Keys
from selenium.webdriver.common.keys import Keys




