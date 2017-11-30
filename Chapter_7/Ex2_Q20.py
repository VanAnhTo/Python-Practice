import  re

#regex = re.compile(r'(\d{1,2})(,\d{3})*')

#regex = re.compile(r'^\d{1,3}(,\d{3})*$')

regex = re.compile(r'^([A-Z]){1}(\w)+?\s(N)(akamoto)$')

n = regex.search('satoshi Nakamoto').group()
print(n)