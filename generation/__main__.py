from openpyxl import load_workbook
from random_physicalculture import Data_Geranate

wb = load_workbook(filename='download.xlsx')
sheets = wb.sheetnames

wr = wb.active

wr['A19'] = 'SSSSS'

col = 4

for row in range(19, 25):
        _ = wr.cell(column=col, row=row, value="{0}".format(Data_Geranate.gen_pulse()))
        print(_)

wb.save('dow.xlsx')
