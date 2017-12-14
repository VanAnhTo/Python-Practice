import shutil, os, re

imgFolder = "D:\\AnhTo\\Draft\\img\\"
for folder,subfolders, fileNames in os.walk(imgFolder):

    print('FOLDER NAME is: '+folder)

    for subfolder in subfolders:
        print("SUBFOLDER NAME is : " + subfolder)

    for fileName in fileNames:

        print('FILE NAME: '+fileName)
        fileInfo = fileName.get
        #Get file size
        #if > 100M > Print out absolute path and file name 
            

    print('\n')
