INCH = 12
YARD = 3
MILE = 5280

print("Enter the distance in feet: .")
distanceInFeet: float = float(input())

feetInInches: float = float(distanceInFeet * INCH)
print("The distance in inches is: %.2f" %feetInInches)

feetInYards: float = float(distanceInFeet / YARD)
print("The distance in yards is: %.2f" %feetInYards)

feetInMiles: float = float(distanceInFeet / MILE)
print("The distance in miles is: %.9f" %feetInMiles)