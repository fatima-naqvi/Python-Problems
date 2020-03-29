TOONIES = 200
LOONIES = 100
QUARTERS = 25
DIMES = 10
NICKLE = 5
PENNIES = 1

#input
print("Enter the amount of money you want to turn into coins : ")
amountOfMoney : int = int(input())

#toonies
# noinspection PyTypeChecker
amountOfToonies: int = int(amountOfMoney / TOONIES)
amountOfMoney : int = amountOfMoney % TOONIES
if amountOfToonies > 0:
    print ("Toonies:  %d" %amountOfToonies)
#print ("You will get %d amountOfMoney." %amountOfMoney)


# # noinspection PyTypeChecker
amountOfLoonies : int = int(amountOfMoney / LOONIES)
amountOfMoney : int = amountOfMoney % LOONIES
if amountOfLoonies > 0:
    print ("Loonies:  %d" %amountOfLoonies)
#print ("You will get %d amountOfMoney." %amountOfMoney)


#quaters
 # noinspection PyTypeChecker
amountOfQuarters: int = int(amountOfMoney / QUARTERS)
amountOfMoney: int = amountOfMoney % QUARTERS
if amountOfQuarters > 0:
    print("Quarters: %d" %amountOfQuarters)
#print ("You will get %d amountOfMoney." %amountOfMoney)


#dimes
# noinspection PyTypeChecker
amountOfDimes: int = int(amountOfMoney / DIMES)
amountOfMoney: int = amountOfMoney % DIMES
if amountOfDimes > 0:
    print("Dimes:    %d" %amountOfDimes)
#print ("You will get %d amountOfMoney." %amountOfMoney)


#nickle
#noinspection PyTypeChecker
amountOfNickles: int = int(amountOfMoney / NICKLE)
amountOfMoney: int = amountOfMoney % NICKLE
if amountOfNickles > 0:
    print("Nickles:  %d" %amountOfNickles)
#print ("You will get %d amountOfMoney." %amountOfMoney)


#pennies
#noinspection PyTypeChecker
amountOfPennies: int = int(amountOfMoney / PENNIES)
if amountOfPennies > 0:
    print("Pennies:  %d" %amountOfMoney)
#print ("You will get %d amountOfMoney." %amountOfMoney)

