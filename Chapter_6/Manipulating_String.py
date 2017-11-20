spam = "That is Alice's cat."
#Manipulating string


#print(spam)

#Escape Characters
'''
\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash

print('Say hi to Bob\'s mother.')
print("Hello there!\nHow are you?\nI\'m doing fine.")
'''

# raw string: A raw string completely ignores all escape characters and
#             prints any backslash that appears in the string
# Raw strings are helpful if you are typing string values that contain many backslashes
'''
print(r'That is Carol\'s cat.')
'''

'''
#Mutiline with trible quote

print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

'''

#indexing and slicing strings
spam = 'Hello world!'
'''
print(spam[1])
print(spam[:5])
print(spam[6:])
fizz = spam[0:7]
print(fizz)
'''
#the in and not in operators strings
'''
print('Hello' in 'Hello world!')
print('Hellos' in spam)

print('bon' not in spam)
'''

#upper(), lower(), isupper(), islower() string method
'''
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

spam = spam.upper().lower().upper()
print(spam)

print(spam.isupper())
print(spam.islower())
'''

#isX string method:
'''
#isalpha() returns True if the string consists only of letters and is not blank

#print('Hello'.isalpha())

#isalnum() returns True if the string consists only of letters and numbers and is not blank

#print('HelLO30'.isalnum())

#isdecimal() returns True if the string consists only of numeric characters and is not blank
#print('1234'.isdecimal())

#isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.

#print('\t '.isspace())

#istitle() returns True if the string consists only of words
# that begin with an uppercase letter followed by only lowercase letters.
print('This Is A T123 Letter'.istitle())

'''
#The startswith() and endswith() method:
'''
print('Hello world'.startswith('Hello world'))
print('Van Anh'.endswith('123 Anh'))
print('Vananh123'.startswith('Van'))
print('Vananh1234'.endswith('1234'))
'''

#the join() and split() string method:
'''
spam1 = 'this is my boyfriend123'
spam = ['this', 'is','my', 'boyfriend']

print(', '.join(spam))
print('123'.join(spam))

print(spam1.split())
print(spam1.split('123'))
print(spam1.split('s'))
'''

#Justifying text with rjust(), ljust() and center()
'''
print('Van Anh'.rjust(20)) #total length of string, space added from 0 = 20
print('To Van Anh'.rjust(20))

print('Van Anh'.rjust(20,'$')) #the $ to be add to the string >> length of string= 20
print('Van Anh'.ljust(20, '@')) #the character added from the last character of string, length = 20

print('VanAnh'.center(20,'*')) 
'''

#removing whitespace with strip(), rstrip(), lstrip()
'''
spam = '       VanAnh          '
print(spam.strip())

print(spam.lstrip())

print(spam.rsplit())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('Samp'))
'''
#Copy and paste string with pyperclip module:
#Ex4






