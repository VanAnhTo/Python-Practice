tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['dogs1', 'cats17777', 'moose31', 'goose133']]

x = len(tableData)
y = len(tableData[0])

colWith = [0]* len(tableData)

for i in range (x):
   colWith[i] = len(max(tableData[i], key = len))


a =''

for i in range(y):
    for j in range(x):
        if j == x - 1:
            a = a + '  ' + tableData[j][i].rjust(colWith[j],' ') + '\n'
        else:
            a = a + '  ' + tableData[j][i].rjust(colWith[j],' ')
print (a)