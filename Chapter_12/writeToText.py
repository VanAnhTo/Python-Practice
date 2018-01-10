import os,shutil
import openpyxl
import sys
import openpyxl.cell
from numpy.distutils.system_info import numarray_info
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter, column_index_from_string

excelFile = '1.xlsx'
wb = openpyxl.load_workbook(excelFile)
sheet = wb.get_sheet_by_name('Sheet')

