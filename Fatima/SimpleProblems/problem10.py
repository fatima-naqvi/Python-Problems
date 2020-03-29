print("Enter a number : ")
firstNumber: int = int(input())

print("Enter a different number : ")
secondNumber: int = int(input())

sumOfFirstNumberAndSecondNumber: int = firstNumber + secondNumber
differenceOfSecondNumberAndFirstNumber: int = secondNumber - firstNumber
productOfFirstNumberAndSecondNumber: int = firstNumber * secondNumber
# noinspection PyTypeChecker
quotientOfFirstNumberAndSecondNumber: int = firstNumber / secondNumber


print("The sum of %d and %d is : %d" %(firstNumber,secondNumber,sumOfFirstNumberAndSecondNumber))
print("The difference between %d and %d is : %d" %(secondNumber,firstNumber,differenceOfSecondNumberAndFirstNumber))
print("The product of %d and %d is : %d" %(firstNumber,secondNumber,productOfFirstNumberAndSecondNumber))
print("The quotient of %d and %d is : %d" %(firstNumber,secondNumber,quotientOfFirstNumberAndSecondNumber))


