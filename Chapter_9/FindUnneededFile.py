import shutil, os, re

imgFolder = "E:\\Draft\\"
for folder, subfolders, fileNames in os.walk(imgFolder):

    print('FOLDER NAME is: '+folder)

    for subfolder in subfolders:
        print("SUBFOLDER NAME is : " + subfolder)

    for fileName in fileNames:
        #print('FILE NAME: '+fileName)
        size = os.path.getsize(folder+'\\'+fileName)
        if size > 31543536:
            print('File: ' + folder+'\\'+fileName )

        #Get file size
        #if > 100M > Print out absolute path and file name 
            

    print('\n')
