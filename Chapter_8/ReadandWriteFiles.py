import os
import shelve
import pprint
import myCats

#------------
#Backslash on Windows
'''
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('D:\\AnhTo\\git\\Pycharm\\Draft', filename))
#D:\AnhTo\git\Pycharm\Draft\accounts.txt
#D:\AnhTo\git\Pycharm\Draft\details.csv
#D:\AnhTo\git\Pycharm\Draft\invite.docx
'''

#The Current Working Directory
'''
print( os.getcwd())
#D:\AnhTo\git\Pycharm\Automated_boring_stuff\Chapter_7

os.chdir('C:\\Windows\\System32')
print(os.getcwd())
#C:\Windows\System32
'''

#Handling Absolute and Relative Paths
# os.path.abspath(path) : Return a string of the absolute path ò the argument
# os.path.isabs(path): return True if the argument is an absolute path.
# os.path.relpath(path, start): return a string of a relative path from the start path to path
'''
print(os.path.abspath('.'))
#D:\AnhTo\git\Pycharm\Automated_boring_stuff\Chapter_7

print(os.path.abspath('.\\Chapter_7'))
#D:\AnhTo\git\Pycharm\Automated_boring_stuff\Chapter_7\Chapter_7

print(os.path.isabs('.'))
#False

print(os.path.isabs(os.path.abspath('.')))
#True

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
#calc.exe

print(os.path.dirname(path))
#C:\Windows\System32

print(os.path.split(path))
#('C:\\Windows\\System32', 'calc.exe')

print((os.path.dirname(path), os.path.basename(path)))
#('C:\\Windows\\System32', 'calc.exe')

print(path.split(os.path.sep))
#['C:', 'Windows', 'System32', 'calc.exe']
'''

#Finding File Sizes and Folder Contents
# os.path.getsize(path): return the size in bytes of the file in the path argument
# os.listdir(path): return a list of filename strings for each file in the path argument
'''
print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
#918528

print(os.listdir('D:\\AnhTo\\Git\\Project'))
#['Bootstrap', 'Eclipse', 'IBM-master', 'IBM-master.zip', 'XcartTestNG', 'XcartTestNG.rar']
'''
#----------------

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





