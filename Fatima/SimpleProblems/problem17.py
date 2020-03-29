#Problem # 25

SECOND = 60
SECONDS_IN_MINUTE = 60 #seconds
HOURS = 60 #minutes
DAYS = 24 #hours

print("Enter the time in seconds:")
numberOfSeconds: int = int(input())

#seconds to minutes
minutes: int = int(numberOfSeconds / 60)
numberOfSeconds: int = int(numberOfSeconds % 60)

#minuts to hours
hours: int = int(minutes / 60)
leftOverMinutes:int = int(minutes % 60)

#hours to days
days: int = int(hours / 24)
leftOverHours: int = int(hours % 24)

print("%d:%.2d:%.2d:%.2d" % (days, leftOverHours, leftOverMinutes, numberOfSeconds))








