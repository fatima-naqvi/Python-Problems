print("Enter the year you were born in.")
year: int = int (input())

remainder: int = int(year % 12)

if remainder == 8 :
    print("Your Chinese Zodiac is a Dragon.")
elif remainder == 9 :
    print("Your Chinese Zodiac is a Snake.")
elif remainder == 10 :
    print("Your Chinese Zodiac is a Horse.")
elif remainder ==  11:
    print("Your Chinese Zodiac is a Sheep.")
elif remainder == 0 :
    print("Your Chinese Zodiac is a Monkey.")
elif remainder == 1 :
    print("Your Chinese Zodiac is a Rooster.")
elif remainder == 2 :
    print("Your Chinese Zodiac is a Dog.")
elif remainder == 3 :
    print("Your Chinese Zodiac is a Pig.")
elif remainder == 4 :
    print("Your Chinese Zodiac is a Rat.")
elif remainder == 5 :
    print("Your Chinese Zodiac is a Ox.")
elif remainder == 6 :
    print("Your Chinese Zodiac is a Tiger.")
elif remainder == 7 :
    print("Your Chinese Zodiac is a Hare.")
print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")