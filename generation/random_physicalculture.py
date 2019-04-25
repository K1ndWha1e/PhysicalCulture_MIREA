from generation.classes import *


class Data_Generate():
    def gen_timesleep(self):
        timesleep = TimeSleep().rand_timesleep()

        return timesleep

    def gen_appetite(self):
        appetitte = Appetite().rand_appetite()

        return appetitte

    def gen_pulse():
        pulse = HeartBeat().rand_heartbeat()

        return pulse

    def gen_weight():
        weight = Weights().rand_weights(80)

        return weight

    def gen_gymnastic():
        gymnastic = MorningGymnastics().rand_morning_gymnastics()

        return gymnastic

    def gen_name_physical_culture():
        list_name_physical_culture = []

        name_physical_culture = NamePhysicalCulture().rand_physicalculture()

        list_name_physical_culture.append(name_physical_culture)

        return name_physical_culture

    def gen_counts_exercises(self, name_physical_culture):

        counts_exercises = Counts_Exercises().rand_countsphysical(name_physical_culture)

        return counts_exercises


    def gen_conclusion(self, counts_exercises):
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


    def gen_feel(self):
        feel = Feel().rand_feel()
        return feel