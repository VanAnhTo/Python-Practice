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

# Searching for Email

# Selecting a Folder
pprint.pprint(imapObj.list_folders())

imapObj.select_folder('INBOX', readonly=True)

# Performing the Search

print(imapObj.search(['ALL']))
imapObj.search(['ON 05-Feb-2018'])

imapObj.search(['SINCE 05-Jan-2017', 'BEFORE 05-Feb-2018', 'UNSEEN'])
imapObj.search(['SINCE 05-Jan-2017', 'FROM alice@example.com'])
imapObj.search(['SINCE 05-Jan-2017', 'NOT FROM alice@example.com'])
imapObj.search(['OR FROM alice@example.com FROM bob@example.com'])
imapObj.search(['FROM alice@example.com', 'FROM bob@example.com'])

#****The search() method doesn’t return the emails themselves
# but rather unique IDs (UIDs) for the emails, as integer values

#Size Limits
#***This limit is in place to prevent your Python programs from eating up too much memory
# the default size limit is often too small.You can change this limit
# from 10,000 bytes to 10,000,000 bytes by running this code:

imaplib._MAXLINE = 10000000

#If you are logging in to a Gmail account,
# pass the search terms to the gmail_search() method instead of the search() method
UIDs = imapObj.gmail_search('meaning of life')

#Fetching an Email and Marking It As Read
#you have a list of UIDs, you can call the IMAPClient object’s fetch() method to get the actual email content

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawMessages)


#Getting Email Addresses from a Raw Message
message = pyzmail.PyzMessage.factory(rawMessages[5]['BODY[]'])

print(message.get_subject())
print('From******:' + message.get_addresses('from'))
print('To******:' + message.get_addresses('to'))
print('CC******:' + message.get_addresses('cc'))
print('BCC******:' + message.get_addresses('bcc'))

#Getting the Body from a Raw Message

message.text_part.get_payload().decode(message.text_part.charset)
message.html_part.get_payload().decode(message.html_part.charset)
