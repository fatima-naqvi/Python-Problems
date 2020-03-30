CONVERSION_1 = 10.5
CONVERSION_2 = 4

print("Enter the number of human years:")
humanYr: float = float(input())
dogYears : float = 0.0

if humanYr <= 2 :
    dogYears: float = float(humanYr * CONVERSION_1)
else :
    dogYears = float(2 * CONVERSION_1) # first 2 years
    dogYears = float((humanYr-2) * CONVERSION_2) # 3rd year and above.s

print("%d human years ===> %.2f dog years" % (humanYr, dogYears))
