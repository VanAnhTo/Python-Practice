import re
import os

print(os.getcwd())
path = 'E:\\Project\\Python_Project\\Python-Practice\\Chapter_8\\TestFolder'
print (os.listdir(path))

folder = os.listdir(path)

regex = re.compile(r'.*.txt')
regexCat = re.compile('cat')

for i in range(len(folder)):
    a = folder[i]
    print(a)
    if regex.search(a) != None:
        contentFile = open(path +'\\' +a)
        content = contentFile.read()
        searchCat = regexCat.search(content)
        print(searchCat)

