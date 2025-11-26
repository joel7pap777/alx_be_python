FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

temperature = float(input('enter the temperature to convert:'))
def convert_to_celsius(fahrenheit):
    fahrenheit= (temperature-32) *FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temperature}°F is {fahrenheit}°C")
    
def  convert_to_fahrenheit(celsius):
    celsius = (temperature-32) *CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{temperature}°C is {celsius}°F")


user_temperature = input('Is this temperature in Celsius or Fahrenheit? (C/F):').upper()

if(user_temperature=='F'):
    convert_to_celsius(temperature)
  
elif(user_temperature=='C'):
 convert_to_fahrenheit(temperature)
 
else:
    print("Invalid temperature. Please enter a numeric value.")