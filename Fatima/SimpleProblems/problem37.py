print("Enter an amount of 3 - 10 sides :")
sides: int = int(input())

if sides <= 2 :
    print("Invalid input. Please enter 3 and above.")
elif sides == 3 :
    print("Your shape is a triangle.")
elif sides == 4 :
    print(" Your shape is a square.")
elif sides == 5 :
    print("Your shape is a pentagon.")
elif sides == 6 :
    print("Your shape is a hexagon.")
elif sides == 7 :
    print("Your shape is a heptagon.")
elif sides == 8 :
    print("Your shape is a octagon.")
elif sides == 9 :
    print("Your shape is a nonagon.")
elif sides == 10 :
    print("Your shape is a decagon.")
else :
    print("You put more/less amount of sides.")

