import shutil, os, re

imgFolder = "D:\\AnhTo\\Draft\\img\\"
for folder,subfolders, fileNames in os.walk(imgFolder):

    #print('FOLDER NAME is: '+folder)

    for subfolder in subfolders:
        print("SUBFOLDER NAME is : " + subfolder)

    for fileName in fileNames:

        #print('FILE NAME: '+fileName)
        size = os.path.getsize(folder + '\\' + fileName)
        if size > 12798:
            print('File: ' + folder + '\\' + fileName)


    print('\n')
