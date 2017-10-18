spam = ['cat', 'bat', 'rat', 'elephant']

#List
'''
print(spam)
print (spam[0])
print ('hello ' + spam[3])
print ('The '+ spam [1] + ' eat the ' + spam [2] + '.')
#print (spam[100])

spam = [['cat', 'dog'], [11, 14,  16, 20]]
print (spam)

#in ra phan tu thu 2 trong list dau tien cua spam = dog
print(spam[0][1])

#in ra phan tu thu 3 trong list thu 2 cua spam = 16.
print (spam [1][2])
'''

## NEGATIVE INDEX
'''
# -1 = last index in list, -2 = second-to-last index in a list
spam = ['cat', 'bat', 'rat', 'elephant']
print (spam[-1])
print(spam[0:4])
print(spam[1:3])
print (spam[0:-1])

print (spam[:2])
print (spam[1:])
print (spam[:])

#length of the list

print (len(spam))
'''

#Change value in list with index:
'''
spam[1] = 'tiger'
print (spam)

spam[2] = spam[1]
print (spam)
'''

#list concatenation and list replication
'''
print ([1,2,3] + ['A', 'B', 'C'])

print (['A', 'B', 'C'] * 3)

spam = spam + ['lion', 'cow']
print (spam)
'''

# removing value from list with del statement
'''
del (spam [-1])
print (spam)
'''

#for loop with list
'''
for i in range(3):
    print (i)

for i in [1,2,3,4,5]:
    print (i)

for i in range(len(spam)):
    print ('index ' + str(i) + ' in spam is ' + spam[i])
'''

# the in and not in operator

#the in and not in operator

'''
spam = ['hello', 'vananh', 'howdy', 'windy']

print('vananh' in spam)

print ('vananh' not in spam)
'''

# multiple assignment trick
'''
dog = ['fat', 'black', 'run']

size = dog[0]
color = dog[1]
action = dog[2]

print(dog)
print(size, color,action)
'''

#augmented assignment opetators
'''
spam = 12
spam += 2
print (spam)

flower = ['rose']
flower = flower *4
print(flower)
'''

# append

spam = ['rose']
spam.append('tulip')

print(spam)

#insert
spam.insert(1, 'blue')
print (spam)

#remove

spam.remove('tulip')
print(spam)

#sort
spam.sort()
print(spam)

