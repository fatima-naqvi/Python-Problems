print("Enter a month :")
month = input()
orgMonth = month
month = month.lower()

print("Enter a day: ")
day: int = int(input())

if month == 'january' and day == 1 :
    print("The holiday on this day is New Years.")
elif month == 'july' and day == 1 :
    print("The holiday on this day is Canada day.")
elif month == 'december' and day == 25 :
    print("The holiday on this day is Christmas.")
else :
    print("The date that you entered did not correspond with a Canadian holiday.")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


