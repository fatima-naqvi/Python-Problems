#constants
TAX_RATE = .0925
TIP_RATE = .18

#input
print("Enter the meal cost : ")
mealCost: float = float(input())

#calculations
tax: float = mealCost * TAX_RATE
tip:float = mealCost * TIP_RATE
total: float = mealCost + tip + tax

#output
print("Your meal is $%.2f" %mealCost)
print("Your tax is $%.2f" %tax)
print("Your tip is $%.2f" %tip)
print("---------------------")
print("Your total is $%.2f" %total)


