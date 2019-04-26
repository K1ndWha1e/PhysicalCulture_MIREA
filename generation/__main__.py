from openpyxl import load_workbook
from generation.data_filling import *


class Welcome_Message:
    def Header(self):
        print('Welcome to the GenCulture')

        surname = input('Enter ur surname\n')
        name = input('Enter ur name\n')
        last_name = input('Enter ur last-name\n')
        study_group = input('Enter name of ur studying group\n')
        date_birthday = input('Enter the date of ur birthday\nExample: 18/09/99\n')

        ws['I9'] = '{0} {1} {2}' .format(surname, name, last_name)
        ws['I10'] = '{0}'.format(study_group)
        ws['I11'] = '{0}'.format(date_birthday)


class Column_Fill:
    def __init__(self, ws):
        self.ws = ws


    def columns_fill(self, count_days_generate, personal_weight):

        first_column = A_Column().column(self.ws, count_days_generate)
        second_column = B_Column().column(self.ws, count_days_generate)
        three_column = C_Column().column(self.ws, count_days_generate)
        four_column = D_Column().column(self.ws, count_days_generate)
        fifth_column = E_Column().column(self.ws, count_days_generate, personal_weight)
        sixth_column = F_Column().column(self.ws, count_days_generate)
        seventh_column = G_AND_H_AND_I_Column().column(self.ws, count_days_generate)
        eighth_column = J_Column().column(self.ws, count_days_generate)


if __name__ == '__main__':
    wb = load_workbook(filename='download.xlsx')
    ws = wb.active

    Welcome_Message().Header()

    personal_weight = int(input('Enter is ur weight?\n'))

    count_days_generate = int(input('How many day did u want to generate?\n'))

    Column_Fill(ws).columns_fill(count_days_generate, personal_weight)

    wb.save('physical_culture.xlsx')
