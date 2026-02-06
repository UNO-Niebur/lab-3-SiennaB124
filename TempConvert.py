#TempConvert.py
#Name: Sienna Bonner
#Date: 2/4/26
#Assignment: Lab 3 temp conversion


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  fahrenheit = float(input("give me a temperature in fahrneheit\n"))
  celcius = (fahrenheit - 32) * 5/9
  celcius = round(celcius, 1)
  print(fahrenheit, "is ", celcius, "degrees celsius.")
if __name__ == '__main__':
  main()
