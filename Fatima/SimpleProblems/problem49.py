print("Enter a magnitude.")
magnitude: float = float(input())

if magnitude < 2.0 :
    print("The description is micro.")
elif (magnitude >= 2.0) and (magnitude < 3.0) :
    print("The description is very minor.")
elif (magnitude >= 3.0) and (magnitude < 4.0) :
    print("The  description is minor.")
elif (magnitude >= 4.0) and (magnitude < 5.0) :
    print("The description is light.")
elif (magnitude >= 5.0) and (magnitude < 6.0):
    print("The description is moderate.")
elif (magnitude >= 6.0) and (magnitude < 7.0) :
    print("The description is strong.")
elif (magnitude >= 7.0) and (magnitude < 8.0) :
    print("The description is major.")
elif (magnitude >= 8.0) and (magnitude < 10.0) :
    print("The description is great.")
elif magnitude > 10.0 :
    print("The description is meteoric.")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")



