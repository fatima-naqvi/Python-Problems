print("Enter a 4 digit number:")
fourDigitNumber: int = int(input())

firstDigitNumber:int = int(fourDigitNumber % 10)
fourDigitNumber:int = int(fourDigitNumber / 10)

secondDigitNumber:int = int(fourDigitNumber % 10)
fourDigitNumber:int = int(fourDigitNumber / 10)

thirdDigitNumber:int = int(fourDigitNumber % 10)
fourDigitNumber:int = int(fourDigitNumber / 10)

fourthDigitNumber:int = int(fourDigitNumber % 10)
fourDigitNumber:int = int(fourDigitNumber / 10)

sumOfAllDigits: int = int(firstDigitNumber + secondDigitNumber + thirdDigitNumber + fourthDigitNumber)
print("%d + %d + %d + %d = %d" %(fourthDigitNumber, thirdDigitNumber, secondDigitNumber, firstDigitNumber, sumOfAllDigits))
