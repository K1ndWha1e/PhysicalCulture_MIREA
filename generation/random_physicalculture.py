from generation import *

appetitte = Appetite().rand_appetite()

pulse = HeartBeat().rand_heartbeat()

weight = Weights().rand_weights(80)

gymnastic = MorningGymnastics().rand_morning_gymnastics()

name_physical_culture = NamePhysicalCulture().rand_physicalculture()

counts_exercises = Counts_Exercises().rand_countsphysical(name_physical_culture)

feel = Feel.rand_feel()

print(appetitte)
print(pulse)
print(weight)
print(gymnastic)
print(name_physical_culture)
print(counts_exercises)
print(feel)