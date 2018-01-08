import os,shutil
import openpyxl
import sys
import openpyxl.cell
from numpy.distutils.system_info import numarray_info
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter, column_index_from_string

folderPath = 'E:\\Project\\Python_Project\\Python-Practice\\Chapter_12\\test\\'

file = 'E:\\Project\\Python_Project\\Python-Practice\\Chapter_12\\test\\test2.txt'
#fileContent = open(file)
'''
with open(file) as f:
    content = f.readlines()

print(content)
'''

excelFile = '1.xlsx'
wb = openpyxl.load_workbook(excelFile)
sheet = wb.get_sheet_by_name('Sheet')
d = 1
for fileName in os.listdir(folderPath):
    print(fileName)
    print(folderPath+fileName)
    with open(folderPath+fileName) as f:
        content = f.readlines()
        print(content)

