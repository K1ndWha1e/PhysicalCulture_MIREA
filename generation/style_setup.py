from openpyxl.styles import Font, Alignment


class Style:
    def style(self, latter_column, ws):
        for cell in ws[latter_column]:
            cell[0].font = Font(name='Times New Roman',
                                size=14,
                                color='FF0000')

            cell[0].alignment = Alignment(horizontal='center',
                                          vertical='center')

