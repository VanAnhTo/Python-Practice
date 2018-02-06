#Sending Email
import smtplib
import imapclient
import pprint

'''
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpObj))

print(smtpObj.ehlo())
#Once you have the SMTP object, call its oddly named ehlo() method to “say hello” to the SMTP email server
#If the first item in the returned tuple is the integer 250 (the code for “success” in SMTP),
# then the greeting succeeded.

#Starting TLS Encryption

print(smtpObj.starttls())
#This required step enables encryption for your connection
#starttls() puts your SMTP connection in TLS mode.
# The 220 in the return value tells you that the server is ready.

#login with email and pass word by using login() method

print(smtpObj.login('anhanh29bg@gmail.com', '******'))

#Sending an Email
# Call the sendmail() method to actually send the email.
smtpObj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com ',
'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')

#Disconnecting from the SMTP Server
print(smtpObj.quit())
'''


imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print(imapObj.login(' anhanh29bg@gmail.com ', '******'))
pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
