tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

x = len(tableData)
y = len(tableData[0])

a =''

for i in range(y):
    for j in range(x):
        if j == x - 1:
            a = a + '  ' + tableData[j][i] + '\n'
        else:
            a = a + '  ' + tableData[j][i]
print (a)