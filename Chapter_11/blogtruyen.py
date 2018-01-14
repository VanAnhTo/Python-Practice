from selenium import webdriver
import requests, bs4, os
from selenium.webdriver.common.keys import Keys

os.makedirs('blogtruyen', exist_ok=True)

rootUrl = 'http://blogtruyen.com'

blogUrl = 'http://blogtruyen.com/17039/isekai-nonbiri-nouka-17039'

res = requests.get(blogUrl)

soup = bs4.BeautifulSoup(res.text, "html.parser")

chapter = soup.select('#list-chapters a')
#print('Number of chapters: '+ str(len(chapter)))

for i in range (len(chapter)):
    chUrl = chapter[i].get('href')
    chapterUrl = rootUrl+chUrl
    print(chapterUrl)

    resChapter = requests.get(chapterUrl)
    soupChapter = bs4.BeautifulSoup(resChapter.text, "html.parser")
    imgPage = soupChapter.select('#content img')
    for j in range(len(imgPage)):
        # print(comicElem[i])
        comicUrl = imgPage[j].get('src')
        print(comicUrl)
        resImg = requests.get(comicUrl)
        resImg.raise_for_status()

        # E:\\Project\\Python_Project\\Python-Practice\\Chapter_11\\
        imageFile = open(os.path.join('blogtruyen', os.path.basename(comicUrl)), 'wb')

        for chunk in resImg.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    print('Done.')



    '''
    chUrl = chapter[i].get('value')
    text = chapter[i].getText()
    #print(text)

    chapterUrl = rootUrl+chUrl

    print('Url of chapter: '+ chapterUrl)

    res = requests.get(blogUrl)

    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    imgPage = soup.select('#content img')

    print('Length of img page: '+ str(len(imgPage)))

    #for j in range(len(imgPage)):

    pageUrl = imgPage[1].get('url')

    res = requests.get(pageUrl)

    res.raise_for_status()

    imageFile = open(os.path.join('blogtruyen', os.path.basename(text+'_page_%s.jpg',j)), 'wb')

    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
'''
'''
blogUrl = 'http://blogtruyen.com/c280309/isekai-nonbiri-nouka-17039-chap-1?sbro=redirect'
os.makedirs('xkcd', exist_ok=True)

res = requests.get(blogUrl)
soup = bs4.BeautifulSoup(res.text, "html.parser")

page = soup.select('#content img')
print(len(page))

print(page[2])
comicUrl = page[2].get('src')

print(comicUrl)
res = requests.get(comicUrl)
res.raise_for_status()

imageFile = open(os.path.join('xkcd', os.path.basename('2.jpg')), 'wb')

for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()



print('Done.')
'''

'''

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

'''