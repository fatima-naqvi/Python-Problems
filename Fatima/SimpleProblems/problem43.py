print("Enter a banknote amount: ")
banknote: int = int(input())

if banknote == 100 :
    print("The banknote has Benjamin Franklin on it.")
elif banknote == 50 :
    print("The banknote has Ulysses S. Grant on it.")
elif banknote == 20 :
    print("The banknote has Andrew Jackson on it.")
elif banknote == 510 :
    print("The banknote has Alexander Hamilton on it.")
elif banknote == 5 :
    print("The banknote has Abraham Lincoln on it.")
elif banknote == 2 :
    print("The banknote has Thomas Jefferson on it.")
elif banknote == 1 :
    print("The banknote has George Washington on it.")
else :
    print("Invalid banknote amount - enter a actual amount.")