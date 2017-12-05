import re

'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
'''

#Groups
'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))

print(mo.group(0))

print(mo.group())

print(mo.groups())

areacode, mainNumber = mo.groups()

print(areacode)
print(mainNumber)
'''
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
#The \( and \) escape characters in the raw string passed to re.compile()
# will match actual parenthesis characters.
'''mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
'''

#Matching multiple groups with the pipe:

#The | character is called a pipe
#Ex: r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'
#When both Batman and Tina Fey occur in the searched string,
# the first occurrence of matching text will be returned as the Match object
'''
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

print(mo.group())

print(mo.group(1))
'''

#Options matching with the question mark
#(abc)?
'''
batRegex = re.compile(r'Bat(anh)?man')

mo1 = batRegex.search('The Adventures of Batman')
#(anh)?

print(mo1.group())
#Batman

mo2 = batRegex.search('The Adventures of Batanhman')
print(mo2.group())
#Batanhman

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo2 = phoneRegex.search('My number is 555-4242')

print(mo1.group())
#415-555-4242
print(mo2.group())
#555-4242
'''

#Matching zero or more with the star
#(abc)*
'''
batRegex = re.compile(r'Bat(anh)*man')
#(anh)*

mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batanhman')
mo3 = batRegex.search('The Adventures of Batanhanhanhman')

print(mo1.group())
#Batman
print(mo2.group())
#Batanhman
print(mo3.group())
#Batanhanhanhoman
'''

#Matching one or more with the plus
#(abc)+
'''
batRegex = re.compile(r'Bat(anh)+man')

mo1 = batRegex.search('The Adventures of Batanhman')
mo2 = batRegex.search('The Adventures of Batanhanhanhman')

mo3 = batRegex.search('The Adventures of Batman')

print(mo1.group())
#Batanhman

print(mo2.group())
#Batanhanhanhman

print(mo3 == None)
#True

'''

#Matching with specific repetition with curly brackets
#(Ha){3} >> HaHaHa - 3 Ha
# (Ha){3,5} >> ((HaHaHa)| (HaHaHaHa) | (HaHaHaHaHa))

'''
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('He laughs: HaHaHa')
print(mo1.group())
#HaHaHa

'''

#Greedy and nongreedy matching
#Python’s regular expressions are greedy by default: will match the longest string possible
#The non-greedy: matches the shortest string possible
'''
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')

print(mo1.group())
#HaHaHaHaHa
print(mo2.group())
#HaHaHa
'''

#Findall method
#search() will return a Match object of the first matched text in the searched string
#findall() method will return the strings of every match in the searched string
'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1)
#['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)
#[('415', '555', '9999'), ('212', '555', '0000')]
'''

#No group: findall() returns a list of string matches: such as ['415-555-9999', '212-555-0000'].
#Groups: findall() returns a list of tuples of strings (one string for each group)
        # such as [('415', '555', '9999'), ('212', '555', '0000')].
'''
xmasRegex = re.compile(r'\d+\s\w+')
str = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
print(xmasRegex.findall(str))
#['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans',
    #  '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
'''
#Regex: \d+\s\w+ : text has one or more digits (\d+), followed by a whitespace (\s),
# followed by one or more letter/digits/underscore (\w+),
# findall() returns all matching strings of the regex pattern in a list
#-------------------------------------------------

#Making character classes
'''
#[aeiouAEIOU] will match any vowel, both lowercase and uppercase
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo1)

#character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers
#negative character class: [^aeiouAEIOU]: will match all the characters that are not in the character class

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo2 = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo2)
'''

#The caret and dollar sign characters

#the caret symbol (^) at the start of a regex:  match must occur at the beginning of the searched text
#dollar sign ($) at the end of the regex: the string must end with this regex pattern
'''
beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
print(mo1)

endsWithNumber = re.compile(r'\d$')
mo2 = endsWithNumber.search('Your number is 42')
print(mo2)

wholeStringIsNum = re.compile(r'^\d+$')
mo3 = wholeStringIsNum.search('1234567890')
print(mo3)
#1234567890

wholeStringIsNum = re.compile(r'^\d+$')
mo4 = wholeStringIsNum.search('12345 and 67890')
print(mo4)
#None 
'''

#The Wildcard Character
#The . (or dot) character in a regular expression
# is called a wildcard and will match any character except for a newline
'''
atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')

print(mo1)
#['cat', 'hat', 'sat', 'lat', 'mat']

# ****** the dot character will match just one character: flat >>  lat
'''

#Matching Everything with Dot-Star
#dot character means “any single character except the newline
#the star character means “zero or more of the preceding character.
#dot-star (.*) to stand in for that “anything.”
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Elsa Mine Last Name: Moana Frank')
print(mo.group(1))
#Elsa
print(mo.group(2))
#Moana

#dot-star uses greedy mode: always try to match as much text as possible
#all text in a nongreedy fashion, use the dot, star, and question mark (.*?)

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
#<To serve man>

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
#<To serve man> for dinner.>
'''

#Matching Newlines with the Dot Character
#By passing re.DOTALL as the second argument to re.compile(),
# you can make the dot character match all characters, including the newline character
'''
noNewlineRegex = re.compile('.*')
mo1 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo1)
#Serve the public trust. #Not find in newline

newlineRegex = re.compile('.*', re.DOTALL)
mo2 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo2)
#'Serve the public trust.\nProtect the innocent.\nUphold the law.'
'''

#Case-Insensitive Matching
#pass re.IGNORECASE or re.I as a second argument to re.compile()
'''
robocop = re.compile(r'robocop', re.I)
ro1 = robocop.search('Robocop is part man, part machine, all cop.').group()
ro2 = robocop.search('ROBOCOP protects the innocent.').group()
ro3 = robocop.search('Al, why does your programming book talk about robocop so much?').group()

print(ro1) #Robocop
print(ro2) #ROBOCOP
print(ro3) #robocop
'''

#Substituting Strings with the sub() Method
#The first argument is a string to replace any matches
#The second is the string for the regular expression
#The sub() method returns a string with the substitutions applied.
'''
namesRegex = re.compile(r'Agent \w+')
ne1 = namesRegex.sub('Anh To', 'Agent Alice gave the secret documents to Agent Bob.')
print(ne1)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
ne2 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve '
                                     'knew Agent Bob was a double agent.')

print(ne2)
'''

#Managing Complex Regexes


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)


phoneRegex = re.compile(r'('
                        r'(\d{3}|\(\d{3}\))?'
                        r'(\s|-|\.)?'
                        r'\d{3}'
                        r'(\s|-|\.)\d{4} (\s*(ext|x|ext.)'
                        r'\s*\d{2,5})?'
                        r')')

#Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
