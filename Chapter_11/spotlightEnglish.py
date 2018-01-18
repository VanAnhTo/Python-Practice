import requests, os, bs4


res = requests.get('https://spotlightenglish.com')
res.raise_for_status()
spotlightEng = bs4.BeautifulSoup(res.text,"lxml")


items = spotlightEng.select('#recent-programs li a.pull-left')
titles = spotlightEng.select('#recent-programs li aside a')

for i in range (len(items)):
    itemTitle = titles[i].getText()
    itemUrl = items[i].get('href')
    print(itemUrl)

    resItem = requests.get(itemUrl)
    resItem.raise_for_status()
    postContent = bs4.BeautifulSoup(resItem.text, "lxml")
    contents = postContent.select('#transcript p')

    contentPrinted = ''

    for j in range(len(contents)):
        content = contents[j].getText()
        contentPrinted = contentPrinted + '\n' + content
        #print(content)
        #contentS = open(os.path.join('spotlight'), os.path.basename(itemTitle), 'wb')

    contentSave = open(itemTitle + '.txt', 'wb')
    contentSave.write(contentPrinted.encode())
    contentSave.close()

print('Done')





