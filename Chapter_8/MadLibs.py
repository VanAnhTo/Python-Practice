import re

madFile = open('MadLibTestFile.txt')
madContent = madFile.read()
print(madContent)
madFile.close()
regex = re.compile(r'ADJECTIVE|NOUN|VERB')

mad = regex.findall(madContent)
print(mad)

madFile = open('MadLibTestFile.txt','w')
for i in range (len(mad)):
    if mad[i] == 'ADJECTIVE':
        adj = input('Enter an adjective: ')
        reAdj = re.compile(r'ADJECTIVE')
        madContent = reAdj.sub(adj,madContent)
    if mad[i] == 'NOUN':
        noun = input('Enter a noun: ')
        reNoun = re.compile(r'NOUN')
        mo = reNoun.search(madContent).group()
        madContent = madContent.replace(mo, noun,1)
        print(madContent)
    if mad[i] == 'VERB':
        verb = input('Enter a verb: ')
        reVerb = re.compile(r'VERB')
        madContent = reVerb.sub(verb, madContent)

madFile.write(madContent)
madFile.close()
madFile = open('MadLibTestFile.txt')
madContent = madFile.read()
print(madContent)
madFile.close()