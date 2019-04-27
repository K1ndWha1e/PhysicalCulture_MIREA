from openpyxl.styles import Font, Alignment


class Style:
    def __init__(self, latter_column, ws):
        self.column = latter_column
        self.write = ws

    def style(self):
        for cell in self.write[self.column]:
            cell[0].font = Font(name='Times New Roman',
                                size=14,
                                color='FF0000')

            cell[0].alignment = Alignment(horizontal='center',
                                          vertical='center')