import os
import shelve
import pprint
import myCats
#Opening Files with the open() Function
'''
helloFile = open('E:\download\Skype received files\hello.txt')
helloContent = helloFile.readlines()
print(helloContent)

baconFile = open('bacon.txt', 'a')
baconFile.write('Hello world 3!\n')
baconFile.write('Hello world 43!\n')
baconFile.close()
'''


shelfFile = shelve.open('mydata')
'''
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

'''
'''
print(type(shelfFile))
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
#print(shelfFile['cats'])
shelfFile.close()

'''
#Saving Variables with the pprint.pformat() Function
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
'''
print(pprint.pformat(cats))
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
'''
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])





