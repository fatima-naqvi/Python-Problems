print("Enter a number: ")
firstNumber: int =int(input())
print("This will be (a).")

print("Enter another number:")
secondNumber: int = int(input())
print("This will be (b).")

print("Before switching: (a) %d and (b) %d" %(firstNumber, secondNumber))
print("------------------------------------")

# firstNumberHolder: int = int(firstNumber)
#
# switchedValueOfFirstNumber: int = int(firstNumber + secondNumber)
# firstNumber: int = int(switchedValueOfFirstNumber - firstNumber)
#
# switchedValueOfSecondNumber: int = int(secondNumber + firstNumberHolder)
# secondNumber: int = int(switchedValueOfSecondNumber - secondNumber)
#
# print("After switching: (b) %d and (a) %d" %(firstNumber, secondNumber))
#

holder: int = firstNumber
firstNumber = secondNumber
secondNumber = holder
print("After switching: (a) %d and (b) %d" %(firstNumber, secondNumber))


#try to understand it later-----
# firstNumber = firstNumber + secondNumber
# secondNumber = firstNumber - secondNumber
# firstNumber = firstNumber - secondNumber
# print("After switching: (a) %d and (b) %d" %(firstNumber, secondNumber))

