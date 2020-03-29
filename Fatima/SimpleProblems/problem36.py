print("Enter a letter of the alphabet: ")
letter = input()
orgLetter = letter
letter = letter.lower()

if len(letter) > 1 or (letter < 'a') or (letter > 'z') :
    print("Invalid input - Please enter a vowel.")
    exit(5)

# if (letter < 'a') or (letter > 'z') :
#     print("Invalid input character - Please enter a vowel.")
#     exit(1)

if letter == 'a' or 'e' == letter or 'i' == letter or 'o' == letter or 'u' == letter:
    print("Your letter is vowel %c" %letter )
elif letter == 'y' :
    print("Y is sometimes a vowel." )
else:
    print("Your letter is a constant %c" %letter)
