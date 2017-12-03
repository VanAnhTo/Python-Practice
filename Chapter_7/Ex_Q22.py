import re

#'((Alice)|(Bob)|(Carol))\s((eats)|(pets)|(throws))\s((apples)|(cats)|(baseballs))\.'
regex = re.compile(r'(((Alice)|(Bob)|(Carol))\s((eats)|(pets)|(throws))\s((apples)|(cats)|(baseballs))\.)')
m = regex.search('Bob pets cats.')
print(m)