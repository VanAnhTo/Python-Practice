from selenium import webdriver
import requests, bs4, os
from selenium.webdriver.common.keys import Keys








url = 'http://blogtruyen.com/c288141/senakagurashi-chap-12?sbro=redirect'
os.makedirs('xkcd', exist_ok=True)

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

comicElem = soup.select('#content img')
for i in range (len(comicElem)):
    #print(comicElem[i])

    comicUrl = comicElem[i].get('src')

    print(comicUrl)
    res = requests.get(comicUrl)
    res.raise_for_status()
    #E:\\Project\\Python_Project\\Python-Practice\\Chapter_11\\
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

print('Done.')

