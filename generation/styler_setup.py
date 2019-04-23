from openpyxl import load_workbook
from generation.random_physicalculture import Data_Generate
from openpyxl.styles import Font, Alignment
from openpyxl.styles import NamedStyle

wb = load_workbook(filename='download.xlsx')
sheets = wb.sheetnames


class A_Column:
    def column(self):
        pass

class B_Column:
    def column(self):
        pass

class C_Column:
    def column(self):
        pass

class D_Column:
    def columns(self,ws):

        for row in range(19, 25):
            _ = ws.cell(column=4, row=row, value="{0}".format(Data_Generate.gen_pulse()))
            print(_)

        for cell in ws['D19:D25']:
            cell[0].font = Font(name='Times New Roman',
                                size=14,
                                color='FF0000')

            cell[0].alignment = Alignment(horizontal='center',
                                          vertical='center')



