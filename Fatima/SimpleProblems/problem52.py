print("Enter your grade:")
number: float = float(input())

if number <= 0:
    print("You got an F.")
elif number <= 1:
    print("You got an D.")
elif number <= 1.3:
    print("You got an D+.")
elif number <= 1.7:
    print("You got an C-.")
elif number <= 2:
    print("You got an C.")
elif number <= 2.3:
    print("You got an C+.")
elif number <= 2.7:
    print("You got an B-.")
elif number <= 3:
    print("You got an B.")
elif number <= 3.3:
    print("You got an B+.")
elif number <= 3.7:
    print("You got an A-.")
elif number <= 4:
    print("You got an A.")
elif number > 4:
    print("You got an A+.")
else:
    print("Invalid input - enter a proper grade.")
print("=/=/=/=/=/=/=/=/=/=/=/=/=/=")

