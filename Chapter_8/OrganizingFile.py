#The shutil function to let you copy, move, rename and delete files

import shutil, os

#Copying files and folders
#shutil.copy(source, destination)

sourceFolder = 'D:\\AnhTo\\git\\Pycharm\\Automated_boring_stuff\\Chapter_8\\Test\\'
desdinationFolder = 'D:\\AnhTo\\git\\Pycharm\\Automated_boring_stuff\\Chapter_9\\TestChapter9\\'

'''
#print(os.getcwd())
#print(os.chdir('D:\\AnhTo\\git\\Pycharm\\Automated_boring_stuff\\Chapter_8\\Test'))
print(shutil.copy('D:\\AnhTo\\git\\Pycharm\\Automated_boring_stuff\\Chapter_8\\Test\\_File.txt',
            'D:\\AnhTo\\git\\Pycharm\\Automated_boring_stuff\\Chapter_9\\TestChapter9'))

print(shutil.copytree('D:\\AnhTo\\git\\Pycharm\\Automated_boring_stuff\\Chapter_8\\Test',
            'D:\\AnhTo\\git\\Pycharm\\Automated_boring_stuff\\Chapter_9\\TestChapter9.1'))
'''
#Moving and renaming files and  folders
#shutil.move(source, destination):move the file or folder at the path source to the path destination
# and will return a string of the absolute path of the new location.
#if already have a file name in destination folder the same name with moved file >> it will be overwriten.
'''
print(shutil.move(sourceFolder+'123abc.txt', desdinationFolder))

print(shutil.move(sourceFolder + 'bacon.txt', desdinationFolder+'baconmoved.txt'))
'''

#Permanently Deleting Files and Folders
#os.unlink(path) will delete the file at path.
#os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
#shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted
'''
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)
'''

#Safe Deletes with the send2trash Module

#send2trash() function can only send files to the recycle bin
'''
baconFile = open('TestChapter9\\bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.') #write the content
baconFile.close()
send2trash.send2trash('bacon.txt') 
'''

#Walking a Directory Tree
#os.walk()function will return three values on each iteration through the loop:
#1. A string of the current folder’s name
#2. A list of strings of the folders in the current folder
#3. A list of strings of the files in the current folder
folderPath = "D:\\AnhTo\\Draft\\"
'''
for folderName, subfolders, filenames in os.walk(folderPath):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')
'''

#Compressing Files with the zipfile Module
#namelist(): returns a list of strings for all the files and folders contained in the ZIP file.
'''
os.chdir(folderPath)
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('Cassiophia.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()
'''

#Extracting from ZIP Files
#extractall(): extracts all the files and folders from a ZIP file into the current working directory.
#extract() : method for ZipFile objects will extract a single file from the ZIP file.
#The value that extract() returns is the absolute path to which the file was extracted.
'''
os.chdir(folderPath) # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')

exampleZip.extractall(folderPath+ 'AfterExtractFolder')

exampleZip.extract('Cassiophia.txt')
exampleZip.extract('Cassiophia.txt', folderPath+ 'AfterExtractFolder')
exampleZip.close()
'''

#Creating and Adding to ZIP Files
