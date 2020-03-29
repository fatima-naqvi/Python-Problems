print("Enter the month you were born on in numbers:")
month: int = int(input())

print("Enter the date you were born on:")
date: int = int(input())

if (month == 12 and date  > 21) or (month == 1 and date >= 19) :
    print("Your Zodiac sign is a Capricorn.")
elif (month == 1 and date  > 20) or (month == 2 and date >= 18) :
    print("Your Zodiac sign is a Aquarius.")
elif (month == 2 and date  > 19) or (month == 3 and date >= 20) :
    print("Your Zodiac sign is a Pisces.")
elif (month == 3 and date  > 21) or (month == 4 and date >= 19) :
    print("Your Zodiac sign is a Aries.")
elif (month == 4 and date  > 20) or (month == 5 and date >= 20) :
    print("Your Zodiac sign is a Taurus.")
elif (month == 5 and date  > 21) or (month == 6 and date >= 20) :
    print("Your Zodiac sign is a Gemini.")
elif (month == 6 and date  > 21) or (month == 7 and date >= 22) :
    print("Your Zodiac sign is a Cancer.")
elif (month == 7 and date  > 23) or (month == 8 and date >= 22) :
    print("Your Zodiac sign is a Leo.")
elif (month == 8 and date  > 23) or (month == 9 and date >= 22) :
    print("Your Zodiac sign is a Virgo.")
elif (month == 9 and date  > 23) or (month == 10 and date >= 22) :
    print("Your Zodiac sign is a Libra.")
elif (month == 10 and date  > 23) or (month == 11 and date >= 21) :
    print("Your Zodiac sign is a Scorpio.")
elif (month == 11 and date  > 22) or (month == 12 and date >= 21) :
    print("Your Zodiac sign is a Sagittarius.")
else :
    print("The month and date didn't correspond with any Zodiac signs.")
