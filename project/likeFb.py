import random

from selenium import webdriver
from selenium.webdriver import ActionChains, FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Chrome
'''
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=r'E:\Program\Webdriver\chromedriver.exe', chrome_options= chrome_options)
'''
#Firefox
ffprofile = webdriver.FirefoxProfile();
ffprofile.set_preference("dom.webnotifications.enabled", False);
driver = webdriver.Firefox(executable_path=r'E:\Program\Firefox\geckodriver.exe',firefox_profile=ffprofile )

driver.maximize_window()
driver.get('https://www.facebook.com')

email = driver.find_element_by_id("email")
email.send_keys("anhanh29bg@gmail.com")


pas = driver.find_element_by_id("pass")
pas.send_keys("Xoaixanhchammuoi")


btnLogin = driver.find_element_by_id("loginbutton")
btnLogin.click()

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


'''
driver.get('https://www.facebook.com/photo.php?fbid=185346365628530&set=a.185346415628525.1073741827.100024595031338&type=3&theater')

element_to_hover_over = driver.find_element_by_css_selector(".UFILikeLink")
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
time.sleep(2)
emotionNum = random.randint(0, 5)
driver.execute_script("document.getElementsByClassName('_iuw')[{0}].click()".format(emotionNum))
'''

#driver.execute_script('$("._iuw").click();')

#like = driver.find_element_by_css_selector("div._39n")
#like = driver.find_element_by_css_selector("span[aria-label=\"Like\"]")
#webdriver.ActionChains(driver).move_to_element(like).click(like).perform()
#like.click()

#like = driver.find_elements(By.CSS_SELECTOR,"._iuw")







'''
searchField = driver.find_element_by_name("q")
searchField.send_keys("Anh To Thi Van")

searchBtn = driver.find_element_by_css_selector("button[aria-label=\"Search\"]")
searchBtn.click()
'''