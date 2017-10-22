myCat = {'size': 'fat', 'color':'brown','disposition':'loud'}

# Dictionary: Key-value pair:
'''
myCat = {'size': 'fat', 'color':'brown','disposition':'loud'}
#keys are: size, color, disposition
#value are: fat, brown, loud

print(myCat['size'])
print('My cat has' + myCat['color'] +' fur.')

spam ={1234: 'language', 4455: 'English'}
print(spam)
'''

# The keys(), values() and items() method
#myCat = {'size': 'fat', 'color':'brown','disposition':'loud'}
'''
for value in myCat.values():
    print(value)


for key in myCat.keys():
    print(key)

for item in myCat.items():
    print(item)

spam = {'color':'red', 'name': 'VanAnh', 'age': '25'}
print(spam.keys())

print(list(spam.keys()))

for k, v in spam.items():
    print('Key = '+ k + ', Value =  ' + v)

'''

#Check key or value is exists in a dictionary
'''
spam = {'color':'red', 'name': 'VanAnh', 'age': '25'}
print('name' in spam.keys())
print('VanAnh' in spam.values())
print('age' in spam.values())
'''

#The get() method
#get (key, 0) : 0 is default value, if do not have key , it will return 0
'''
shopItem = {'apple': 10, 'cups':20, 'orage': 15}
print('I want to have ' + str(shopItem.get('cups',0))+ ' cups.')
print('She want to have ' + str(shopItem.get('banana',0)) + ' banana.')
'''

# the setdefault() method
spam = {'name':'vananh', 'age':'25'}
spam.setdefault('color', 'black')
print(spam)

