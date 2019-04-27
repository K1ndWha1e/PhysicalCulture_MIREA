import random


def rand_timesleep():
    time = random.randint(6, 8)

    return time


def rand_appetite():
    appetit = ['Хороший', 'Плохой', 'Хороший', 'Отличный']
    rand_appetite = random.choice(appetit)

    return rand_appetite


def rand_heartbeat():
    rand_pulse = random.randint(60, 75)

    return rand_pulse


def rand_weights(weight):
    minus_weight = weight - 2
    plus_weight = weight + 2
    rand_weight = random.randint(minus_weight, plus_weight)

    return rand_weight



def rand_morning_gymnastics():
    yes_or_no = ['Да', 'Да', 'Нет']
    rand_gymnastics = random.choice(yes_or_no)

    return rand_gymnastics


def rand_physicalculture():
    physical = ['Отжимание от пола', 'Бег', '-', 'Приседания', 'Подтягивания', 'Прыжки через скакалку', 'Пресс',
                'Выпады с гантелей', 'Поднятие гантелей']
    rand_physical = random.choice(physical)

    return rand_physical


def rand_countsphysical(physicalcaulture):
    if physicalcaulture == 'Отжимание от пола':
        number_of_approaches = random.randint(5, 7)
        counts = random.randint(10, 20)
        minutes = random.randint(20, 35)

        final_result = '{0} подх. по {1} раз, {2} мин.'.format(number_of_approaches, counts, minutes)

        return final_result

    elif physicalcaulture == 'Бег':
        distance = random.randint(3, 5)
        rate = ['Низкий', 'Средний', 'Высокий']
        rand_rate = random.choice(rate)

        final_result = '{0} км, темп {1}'.format(distance, rand_rate)

        return final_result

    elif physicalcaulture == '-':
        empty = '-'

        return empty

    elif physicalcaulture == 'Приседания':
        number_of_approaches = random.randint(3, 5)
        counts = random.randint(10, 30)

        final_result = '{0} подх., {1} раз'.format(number_of_approaches, counts)

        return final_result

    elif physicalcaulture == 'Прыжки через скакалку':
        number_of_approaches = random.randint(3, 5)
        counts = random.randint(30, 50)

        final_result = '{0} подх., {1} раз'.format(number_of_approaches, counts)

        return final_result

    elif physicalcaulture == 'Подтягивания':
        number_of_approaches = random.randint(3, 5)
        counts = random.randint(5, 20)

        final_result = '{0} подх., {1} раз'.format(number_of_approaches, counts)

        return final_result

    elif physicalcaulture == 'Пресс':
        number_of_approaches = random.randint(3, 5)
        counts = random.randint(10, 20)

        final_result = '{0} подх., {1} раз'.format(number_of_approaches, counts)

        return final_result

    elif physicalcaulture == 'Выпады с гантелей':
        number_of_approaches = random.randint(3, 5)
        counts = random.randint(10, 15)

        final_result = '{0} подх., {1} раз'.format(number_of_approaches, counts)

        return final_result

    elif physicalcaulture == 'Поднятие гантелей':
        number_of_approaches = random.randint(3, 5)
        counts = random.randint(15, 20)

        final_result = '{0} подх., {1} раз'.format(number_of_approaches, counts)

        return final_result


def rand_feel():
    health = ['Неплохо', 'Нормальное', 'Хорошее', 'Отличное']
    rand_feeling = random.choice(health)

    return rand_feeling