import os
baconFile = open('bacon.txt', 'w')
n = 10
for i in range (n):
    j = i +1
    baconFile.write((n-j)*'0' + (2*j -1)*'1'+ (n-j)*'0'+ '\n')