print("Enter a wavelength: ")
wavelength: int = int(input())

if (wavelength >= 380) and (wavelength < 450):
    print("The color that matches this wavelength is violet.")
elif (wavelength >= 450) and (wavelength < 495):
    print("The color that matches this wavelength is blue.")
elif (wavelength >= 495) and (wavelength < 570):
    print("The color that matches this wavelength is green.")
elif (wavelength >= 570) and (wavelength < 590):
    print("The color that matches this wavelength is yellow.")
elif (wavelength >= 590) and (wavelength < 620):
    print("The color that matches this wavelength is orange.")
elif (wavelength >= 620) and (wavelength < 750):
    print("The color that matches this wavelength is .red")
else:
    print("Invalid input - enter a valid wavelength")
print("><><><><><><><><><><><><><><><><><><><><><><><><><")