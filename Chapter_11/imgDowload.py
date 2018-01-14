from selenium import webdriver
import requests, bs4, os
from selenium.webdriver.common.keys import Keys

#url = 'http://blogtruyen.com/11372/senakagurashi'
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

#comicElem = soup.select('#wrapper img')
comicElem = soup.select('#comic img')

#print(comicElem[0])

comicUrl = 'http:' +comicElem[0].get('src')

print(comicUrl)

res = requests.get(comicUrl)
res.raise_for_status()

imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

print('Done.')

