print("Enter your height in inches:")
height: int = int(input())

print("Enter your weigh pounds:")
weigh: int = int(input())

bodyMassIndex: int = int((weigh / height * height) * 703)

print("Your Body Mass Index (BMI) is: %d" %bodyMassIndex)
