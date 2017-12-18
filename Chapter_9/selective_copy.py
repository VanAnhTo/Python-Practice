import shutil, os, re

imgFolder = "E:\Draft\\img\\"
newImgFolder = "E:\Draft\\img_copy\\"

imageParten = re.compile(r'^(.*)?(.jpg|.png)$',re.I)

for folder, subfolders, fileNames in os.walk(imgFolder):

    print('FOLDER NAME is: '+folder)

    for subfolder in subfolders:
        print("SUBFOLDER NAME is : " + subfolder)

    for fileName in fileNames:
        mo = imageParten.search(fileName)
        if mo == None:
            continue
        print('FILE NAME: '+folder+'\\'+fileName)

        shutil.copy(folder+'\\'+fileName, newImgFolder)

    print('\n')

