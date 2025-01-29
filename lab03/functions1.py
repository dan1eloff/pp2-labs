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

'''def solve(numheads, numlegs):
    rabbits = int((numlegs - 2*numheads)/2)
    chickens = int(numheads - rabbits)
    print(f'Number of rabbits = {rabbits} \nNumber of chickens = {chickens}')

numheads = int(input('Number of heads: '))
numlegs = int(input('Number of legs: '))

solve(numheads,numlegs)'''

'''# 4

def filter_prime(arr):
    print('Prime numbers from the list: ')
    for i in arr:
        a = 2
        check = False
        while i>a:
            if i%a == 0:
                check = False
                break
            else:
                check = True
            a += 1
        if check:
            print(f'{i}',end=" ")     

arr = list(map(int, input('Enter the numbers: ').split()))

filter_prime(arr)'''

'''# 5

def get_permutations(line, prefix=""):
    if len(line) == 0:
        print(prefix)
    else:
        for i in range(len(line)):
            remaining = line[:i] + line[i+1:]
            get_permutations(remaining, prefix + line[i])

line = input("Enter the word: ").strip()
print("All permutations of the line: ")
get_permutations(line)'''


'''from itertools import permutations

def get_permutations():
    line = input("Enter the word: ").strip()
    
    all_permutations = permutations(line)   # перестановка
    
    print("All permutations of the line: ")
    for perm in all_permutations:
        print("".join(perm))    # объединение

get_permutations()'''

'''# 6

from itertools import permutations

def get_permutations():
    words = list(map(str, input("Enter the word: ").split()))
    
    all_permutations = permutations(words)
    
    print("All permutations of the line: ")
    for perm in all_permutations:
        print(" ".join(perm))

get_permutations()'''

'''# 7

def has_33(nums):
    ans = False
    for i in range(1, len(nums)):
        if nums[i] == 3 and nums[i-1] == 3:
            ans = True
            break
    return ans

arr = list(map(int, input("Enter the numbers: ").split()))

print(has_33(arr))'''

'''# 8

def spy_game(nums):
    ans = False
    for i in range(0, len(nums)):
        if nums[i] == 0:
            for j in range(i+1, len(nums)):
                if nums[j] == 0:
                    for k in range(j+1, len(nums)):
                        if nums[k] == 7:
                            ans = True
                            break
    return ans

arr = list(map(int, input("Enter the numbers: ").split()))

print(spy_game(arr))'''

'''# 9

def volume_of_sphere(r):
    V = (4 * 3.14 * r**3)/3   # pi = 3.14
    return V

a = int(input("Enter the radius of a sphere: "))
print(f'Volume of a sphere = {volume_of_sphere(a)}')'''

'''# 10

def unique_list(arr):
    unique_arr = []
    for i in arr:
        a = 0
        for j in arr:
            if i == j:
                a += 1
        if a == 1:
            unique_arr.append(i)
    return unique_arr

var = list(map(int, input("Enter the numbers: ").split()))

print(unique_list(var))'''

'''# 11

def is_palindrome(a):
    if a == a[::-1]:
        print(f'The {a} is a palindrome')
    else:
        print(f'The {a} is not a palindrome')

var = input("Enter a word, phrase or sequence: ")

is_palindrome(var)'''

# 12

def histogram():
    nums  = list(map(int, input("Enter the numbers: ").split()))
    for i in nums:
        pic = '*'*i
        print("".join(pic))
    
histogram()