print("Enter a month: ")
month = input()
#orgMonth = month
month = month.lower()

print("Enter a day: ")
day = input()

if month == 'march' and day == 20 :
    print("This day is when spring starts.")
elif month == 'june' and day == 21 :
    print("This day is when summer starts.")
elif month == 'september' and day == 22 :
    print("This day is when fall starts.")
elif month == 'december' and day == 21 :
    print("This day is when winter starts.")
else :
    print("The date does not correspond with any season.")
print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")