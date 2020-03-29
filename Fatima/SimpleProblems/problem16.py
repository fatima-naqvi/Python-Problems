HOURS_IN_DAY = 24 #hours
MINUTES_IN_HOUR = 60 #minutes
SECONDS_IN_MINUTE = 60 #seconds

print("Enter the number of days:")
numberOfDays: int = int(input())

print("Enter the number of hours:")
numberOfHours: int = int(input())

print("Enter the number of minutes:")
numberOfMinutes: int = int(input())

print("Enter the number of seconds:")
numberOfSeconds: int = int(input())

#calculating, number of seconds in a day
secondsInDay: int = numberOfDays * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

#hours
secondsInHour: int = numberOfHours * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

#minutes
secondsInMinute: int = int(numberOfMinutes * SECONDS_IN_MINUTE)

#total
totalSeconds:int = secondsInDay + secondsInHour + secondsInMinute + numberOfSeconds

print ("The total amount of days, hours, minutes in seconds is: %d" % totalSeconds)
