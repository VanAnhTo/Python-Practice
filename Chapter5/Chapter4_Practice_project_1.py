spam = []
while True:
    print('Enter the item for spam(Or press enter to cancel): ')
    item = input()
    if item == '':
        break
    else:
        spam =spam + [item]

listPrint =''
for i in range(len(spam)):
    if i != len(spam) -1:
        listPrint = listPrint + spam[i] + ', '
    elif i == len(spam) -1:
        listPrint = listPrint + 'and ' + spam[i]
print(listPrint)

