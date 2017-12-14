import shutil, os, re

imgFolder = "D:\\AnhTo\\Draft\\img\\"
newImgFolder = "D:\\AnhTo\\Draft\\img_copy\\"

imageParten = re.compile(r'^(.*)?(.jpg|.png)$',re.I)

for folder,subfolders, fileNames in os.walk(imgFolder):

    print('FOLDER NAME is: '+folder)

    for subfolder in subfolders:
        print("SUBFOLDER NAME is : " + subfolder)

    for fileName in fileNames:
        mo = imageParten.search(fileName)
        if mo == None:
            continue
        print('FILE NAME: '+fileName)

        #shutil.copy(fileName, newImgFolder)
    print('\n')

