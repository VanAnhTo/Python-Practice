import os,shutil
import openpyxl
import sys
import openpyxl.cell
from numpy.distutils.system_info import numarray_info
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter, column_index_from_string

folderPath = 'E:\\Project\\Python_Project\\Python-Practice\\Chapter_12\\test\\'

excelFile = '1.xlsx'
wb = openpyxl.load_workbook(excelFile)
sheet = wb.get_sheet_by_name('Sheet')
col = 1
for fileName in os.listdir(folderPath):
    with open(folderPath+fileName) as f:
        content = f.readlines()
        print(len(content))
        for j in range(1, len(content)+1):
            print(j)
            print(content[j-1])
            sheet.cell(row=j, column=col).value = content[j-1]
        col = col+1

wb.save('1.xlsx')
