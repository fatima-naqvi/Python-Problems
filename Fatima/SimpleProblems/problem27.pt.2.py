print("Enter your height in meters:")
height: int = int(input())

print("Enter your weigh kilograms:")
weigh: int = int(input())

bodyMassIndex: int = int(weigh / height * height)

print("Your Body Mass Index (BMI) is: %d" %bodyMassIndex)
