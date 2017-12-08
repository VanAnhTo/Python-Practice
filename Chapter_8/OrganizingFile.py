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

