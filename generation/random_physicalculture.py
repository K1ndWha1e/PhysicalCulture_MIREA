from generation.data_randomise import *


def gen_timesleep():
    timesleep = rand_timesleep()

    return timesleep

def gen_appetite():
    appetitte = rand_appetite()

    return appetitte

def gen_pulse():
    pulse = rand_heartbeat()

    return pulse

def gen_weight(personal_weight):
    weight = rand_weights(personal_weight)

    return weight

def gen_gymnastic():
    gymnastic = rand_morning_gymnastics()

    return gymnastic

def gen_name_physical_culture():
    list_name_physical_culture = []

    name_physical_culture = rand_physicalculture()

    list_name_physical_culture.append(name_physical_culture)

    return name_physical_culture

def gen_counts_exercises(name_physical_culture):

    counts_exercises = rand_countsphysical(name_physical_culture)

    return counts_exercises


def gen_conclusion(counts_exercises):
    string_result = ''
    result = 1
    temp = 'темп'
    empty = '-'
    minutes = 'мин'
    flag = False

    if minutes in counts_exercises:
        counts_exercises = counts_exercises[:-5]
        flag = True

    if empty in counts_exercises:
        return empty

    if temp in counts_exercises:
        conclusion = '{0} мин.'.format(random.randint(20, 30))
        return conclusion

    if len(counts_exercises) < 17 or flag:
        for buffer in counts_exercises:
            if buffer != ' ':
                string_result += buffer

            if buffer == ' ':
                if string_result.isdigit():
                    result *= int(string_result)

                string_result = ''

        return result


def gen_feel():
    feel = rand_feel()
    return feel