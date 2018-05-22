import openpyxl

# File to be copied
wb = openpyxl.load_workbook("File_Copy.xlsx")  # Add file name
sheet = wb["Score"] # Add Sheet name


new_sheet = wb.create_sheet('Sheet3')


for row in sheet.rows:
    for cell in row:
        new_cell = new_sheet.cell(row=3,
                   col=2, value= sheet['B3'].value)
        if cell.has_style:
            new_cell.font = cell.font
            new_cell.border = cell.border
            new_cell.fill = cell.fill
            new_cell.number_format = cell.number_format
            new_cell.protection = cell.protection
            new_cell.alignment = cell.alignment



