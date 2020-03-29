print("Enter a side length: ")
side1Length: int = int(input())

print("Enter a second side length: ")
side2Length: int = int(input())

print("Enter a third side length: ")
side3Length: int = int(input())

if side1Length == side2Length == side3Length :
    print("Your triangle is a equilateral triangle.")
elif (side3Length == side2Length) or (side2Length == side1Length) or (side1Length == side3Length) :
    print("Your triangle is a isosceles triangle.")
else :
    print("Your triangle is a scalene triangle.")