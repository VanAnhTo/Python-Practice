import shutil, os, re

import sys
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import zipfile


COMMASPACE = ', '


imgFolder = "D:\\AnhTo\\Draft\\"

#infoFile = open('infoFile.txt','w')

attachments = []
newZip = zipfile.ZipFile('attachFile.zip', 'w')

for folder,subfolders, fileNames in os.walk(imgFolder):

    #print('FOLDER NAME is: '+folder)

    for subfolder in subfolders:
        print("SUBFOLDER NAME: " + subfolder)

    for fileName in fileNames:

        #print('FILE NAME: '+fileName)
        size = os.path.getsize(folder + '\\' + fileName)
        if size > 9000:
            print('File: '+ folder + subfolder + '\\' + fileName)
            attachments.append(folder + subfolder + '\\' + fileName)
            newZip.write(folder + subfolder + '\\' + fileName, compress_type=zipfile.ZIP_DEFLATED)
print('\n')

print(attachments)
print(len(attachments))
#infoFile.close()
newZip.close()

#attach and send Gmail
'''
def main():
    sender = 'anhanh29bg@gmail.com'
    gmail_password = '***********'
    recipients = ['vananhto.bg@gmail.com, anhanh29bg@gmail.com']

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Have a nice day!'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    #attachments = ['FULL PATH TO ATTACHMENTS HERE']

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise


if __name__ == '__main__':
    main()

'''
