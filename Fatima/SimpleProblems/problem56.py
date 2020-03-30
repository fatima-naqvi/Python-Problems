MONTHLY_BILL = 15
TAX_PERCENT = .05
ADDITIONAL_AIR_TIME = .25
ADDITIONAL_TEXT_MESSAGES = .15

print("Enter your air time:")
airTime: int = int(input())

print("Enter your text messages amount:")
messagesAmount: int = int(input())

if (airTime <= 50) and (messagesAmount <= 50):
    taxWithOutTotalMoney: float = float(TAX_PERCENT * MONTHLY_BILL)
    totalMoneyWithTax: float = float(MONTHLY_BILL + taxWithOutTotalMoney)
    print("Monthly payment: $%.2f" % MONTHLY_BILL)
    print("Tax: $%.2f" % taxWithOutTotalMoney)
    print("Total: $%.2f" % totalMoneyWithTax)
elif (airTime > 50) and (messagesAmount > 50):
    calculationsForAirTime1: float = float(airTime - 50)
    calculationsForAirTime2: float = float(calculationsForAirTime1 * ADDITIONAL_AIR_TIME)
    calculationsForTextMessages1: float = float(messagesAmount - 50)
    calculationsForTextMessages2: float = float(calculationsForAirTime1 * ADDITIONAL_TEXT_MESSAGES)
    total: float = float(calculationsForAirTime2 + calculationsForTextMessages2 + MONTHLY_BILL)
    taxWithOutTotalMoney: float = float(TAX_PERCENT * total)
    totalMoneyWithTax: float = float(total + taxWithOutTotalMoney)
    print("Monthly payment: $%.2f" % total)
    print("Tax: $%.2f" % taxWithOutTotalMoney)
    print("Total: $%.2f" % totalMoneyWithTax)
else:
    print("Invalid input.")
print("<<<<<<<<<<<<<...>>>>>>>>>>>>")
