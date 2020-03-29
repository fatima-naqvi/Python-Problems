FEET = 12
CENTIMETER = 2.54

print("Enter you height in feet: ")
heightInFeet: float = float(input())

print("Enter your height in inches: ")
heightInInches: float = float(input())

feetInInches: float = float(heightInFeet * FEET)

inchesInCentimetersAndFeet: float = float(feetInInches * CENTIMETER)

print("Your height in centimeters is: %.2f centimeters." %inchesInCentimetersAndFeet)



