from generation.random_physicalculture import *
from generation.style_setup import Style
from random import randint


def A_Column(ws, count_days_generate):
    last_point = 16 + count_days_generate

    for i, row in enumerate(range(17, last_point)):
        _ = ws.cell(column=1, row=row, value="=(A{0} + {1})".format(16 + i, randint(1, 3)))

    latter = 'A16:A{0}'.format(last_point)
    Style(latter, ws).style()


def B_Column(ws, count_days_generate):
    last_point = 16 + count_days_generate

    for row in range(16, last_point):
        _ = ws.cell(column=2, row=row, value="{0}".format(gen_timesleep()))

    latter = 'B16:B{0}'.format(last_point)
    Style(latter, ws).style()


def C_Column(ws, count_days_generate):
    last_point = 16 + count_days_generate

    for row in range(16, last_point):
        _ = ws.cell(column=3, row=row, value="{0}".format(gen_appetite()))

    latter = 'C16:C{0}'.format(last_point)
    Style(latter, ws).style()


def D_Column(ws, count_days_generate):

    last_point = 16 + count_days_generate
    for row in range(16, last_point):
        _ = ws.cell(column=4, row=row, value="{0}".format(gen_pulse()))

    latter = 'D16:D{0}'.format(last_point)
    Style(latter, ws).style()


def E_Column(ws, count_days_generate, personal_weight):
    last_point = 16 + count_days_generate

    for row in range(16, last_point):
        _ = ws.cell(column=5, row=row, value="{0}".format(gen_weight(personal_weight)))

    latter = 'E16:E{0}'.format(last_point)
    Style(latter, ws).style()


def F_Column(ws, count_days_generate):
    last_point = 16 + count_days_generate

    for row in range(16, last_point):
        _ = ws.cell(column=6, row=row, value="{0}".format(gen_gymnastic()))

    latter = 'F16:F{0}'.format(last_point)
    Style(latter, ws).style()


def G_AND_H_AND_I_Column(ws, count_days_generate):
    list_name_physical_culture = []
    last_point = 16 + count_days_generate

    for i, row in enumerate(range(16, last_point)):
        _ = ws.cell(column=7, row=row, value="{0}".format(gen_name_physical_culture()))
        list_name_physical_culture.append(_.value)

    list_count_physical_culture = []

    for i, row in enumerate(range(16, last_point)):
        _ = ws.cell(column=8, row=row, value="{0}".format(gen_counts_exercises(list_name_physical_culture[i])))
        list_count_physical_culture.append(_.value)

    for i, row in enumerate(range(16, last_point)):
        _ = ws.cell(column=9, row=row, value="{0}".format(gen_conclusion(list_count_physical_culture[i])))

    latter = 'G16:G{0}'.format(last_point)
    Style(latter, ws).style()

    latter = 'H16:H{0}'.format(last_point)
    Style(latter, ws).style()

    latter = 'I16:I{0}'.format(last_point)
    Style(latter, ws).style()

    return list_name_physical_culture


def J_Column(ws, count_days_generate):
    last_point = 16 + count_days_generate

    for i, row in enumerate(range(16, last_point)):
        _ = ws.cell(column=10, row=row, value="{0}".format(gen_feel()))

    latter = 'J16:J{0}'.format(last_point)
    Style(latter, ws).style()