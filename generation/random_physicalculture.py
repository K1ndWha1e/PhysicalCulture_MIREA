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
        counts_exercises_and_results = Counts_Exercises().rand_countsphysical(name_physical_culture)
        print(name_physical_culture)
        print(counts_exercises_and_results[0])

        return counts_exercises_and_results[0]


    def gen_conclusion():
        return result


    def gen_feel():
        feel = Feel().rand_feel()
        return feel
