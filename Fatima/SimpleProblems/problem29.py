print("Enter the temperature in celsius: ")
tempInCelsius: float = float(input())

celsiusToFahrenheit:float = float((tempInCelsius * 9/5) + 32)
print("The temperature in fahrenheit is: %.2f" %celsiusToFahrenheit)

celsiusToKelvin: float = float(tempInCelsius + 273.15)
print("The temperature in kelvin is: %.2f" %celsiusToKelvin)