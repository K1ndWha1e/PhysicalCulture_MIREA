from generation import *

class Data_Generate():
    def gen_timesleep():
        timesleep = TimeSleep.rand_timesleep()
        return timesleep

    def gen_appetite():
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
        global name_physical_culture

        name_physical_culture = NamePhysicalCulture().rand_physicalculture()

        return name_physical_culture

    def gen_counts_exercises():
        global result

        counts_exercises_and_results = Counts_Exercises().rand_countsphysical(name_physical_culture)

        counts_exercises = counts_exercises_and_results[0]

        result = counts_exercises_and_results[1]

        return counts_exercises

    def gen_conclusion():
        return result

    def gen_feel():
        feel = Feel().rand_feel()
        return feel


