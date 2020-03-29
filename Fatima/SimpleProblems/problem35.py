print("Enter the amount of human years:")
humanYr: float = float(input())

if humanYr <= 2 :
    dogYr: float = float(humanYr * 10.5)
    print("%d human years in dog years is: %.2f" %(humanYr, dogYr))

else :
    subtractYr: float = float(humanYr - 2)
    subAndAddYr: float = float(2 * 10.5)
    multiplyYr: float = float(subtractYr * 4)
    doggieYr: float = float(subAndAddYr + multiplyYr)
    print("%d human years in dog years is: %.2f" % (humanYr, doggieYr))



