count: int = 0
while count < 3 :
    print("Enter the length of the field in feet:")
    length: int
    length = int(input())

    print("Enter the width of the field in feet")
    width: int = int(input())

    area: int = length * width
    areaInAcres: float = float(area) / 43560.0

    print("The area of the field is %.2f acres" %areaInAcres)
    print("===========================================")
    count = count + 1

print("Thank you for using my program ---- :)")

