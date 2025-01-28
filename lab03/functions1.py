'''# 1.

def ingredient(grams):
    ounces = 28.3495231 * grams
    return(ounces)

grams = float(input("How many grams: "))
print(ingredient(grams))'''

'''# 2.

def FahrenheittoCelcius(F):
    C = (5/9) * (F-32)
    return C

F = float(input("Temperature in Fahrenheit: "))
print(f"Temperature in Celsius: {FahrenheittoCelcius(F)}")'''

# 3

def solve(numheads, numlegs):
    rabbits = int((numlegs - 2*numheads)/2)
    chickens = int(numheads - rabbits)
    print(f'Number of rabbits = {rabbits} \nNumber of chickens = {chickens}')

numheads = int(input('Number of heads: '))
numlegs = int(input('Number of legs: '))

solve(numheads,numlegs)