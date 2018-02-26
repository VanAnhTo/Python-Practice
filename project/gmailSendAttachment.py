import shutil, os, re

imgFolder = "D:\\AnhTo\\Draft\\img\\"

infoFile = open('infoFile.txt','w')

for fileName in os.listdir(imgFolder):

    #print('File: ' + imgFolder + '\\' + fileName)
    size = os.path.getsize(imgFolder + '\\' + fileName)
    if size > 12798:
        print('File: ' + imgFolder + '\\' + fileName)
        infoFile.write(imgFolder + '\\' + fileName + '\n')

infoFile.close()
