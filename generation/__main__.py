from openpyxl import load_workbook
from generation.styler_setup import *

wb = load_workbook(filename='download.xlsx')
sheets = wb.sheetnames

ws = wb.active

second_column = B_Column().column(ws)
three_column = C_Column().column(ws)
four_column = D_Column().column(ws)
fifth_column = E_Column().column(ws)
sixth_column = F_Column().column(ws)
seventh_column = G_AND_H_Column().column(ws)

wb.save('dow.xlsx')