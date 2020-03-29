#constants
INEREST_PER_YEAR = .04

#input
print("Enter the amount you want to enter in your saving account : ")
amountInSavingAccount: float = float(input()) #$1000

firstYearInterest: float = amountInSavingAccount * INEREST_PER_YEAR #$40
amountInSavingAccount = amountInSavingAccount + firstYearInterest
print("The amount of money you saved in the 1st year is : $%.2f" %amountInSavingAccount)

secondYearInterest: float = amountInSavingAccount * INEREST_PER_YEAR # 2nd year - $41.40
amountInSavingAccount = amountInSavingAccount + secondYearInterest #$1081.60
print("The amount of money you saved in the 2nd year is : $%.2f" %amountInSavingAccount)

thirdYearInterest: float = amountInSavingAccount * INEREST_PER_YEAR # 3rd year
amountInSavingAccount +=  thirdYearInterest
print("The amount of money you saved in the 3th year is : $%.2f" %amountInSavingAccount)

fourthYearInterest: float = amountInSavingAccount * INEREST_PER_YEAR
amountInSavingAccount +=  fourthYearInterest
print("The amount of money you saved in the 4th year is : $%.2f" %amountInSavingAccount)





