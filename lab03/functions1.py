'''# 1.

def ingredient(grams):
    ounces = 28.3495231 * grams
    return(ounces)

grams = float(input("How many grams: "))
print(ingredient(grams))'''

# 2.

def FahrenheittoCelcius(F):
    C = (5/9) * (F-32)
    return C

F = float(input("Temperature in Fahrenheit: "))
print(f"Temperature in Celsius: {FahrenheittoCelcius(F)}")