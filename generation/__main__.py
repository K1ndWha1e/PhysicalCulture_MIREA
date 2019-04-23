from openpyxl import load_workbook
from generation.styler_setup import D_Column

wb = load_workbook(filename='download.xlsx')
sheets = wb.sheetnames

ws = wb.active

column = D_Column().columns(ws)

wb.save('dow.xlsx')
