print("Enter a month:")
month = input()
orgMonth = month
month = month.lower()

if month == 'january' or 'January' or 'JANUARY' :
    print("January has 31.")
elif month == 'february' or 'February' or 'FEBRUARY':
    print("February has days 28 (if its not a leap year) or 29 days (if it is a leap year).")
elif month == 'march' or 'March' or 'MARCH':
    print("March has 31 days.")
elif month == 'april' or 'April' or 'APRIL':
    print("April has 30 days.")
elif month == 'may' or 'May' or 'May':
    print("May has 31 days.")
elif month == 'june' 'June' or 'JUNE':
    print("June has 30 days.")
elif month == 'July' or 'july' or 'JULY':
    print("July has 31 days.")
elif month == 'august' or 'AUGUST'or 'August':
    print("August has 31 days.")
elif month == 'september' or 'September' or 'SEPTEMBER' :
    print("September has 30 days.")
elif month == 'october' or 'October' or 'OCTOBER':
    print("October has 31 days.")
elif month == 'november' or 'November' or 'NOVEMBER':
    print("November has 30 days.")
elif month == 'december' or 'December' or 'DECEMBER' :
    print("December has 31 days.")
else :
    print("That is not a month.")










