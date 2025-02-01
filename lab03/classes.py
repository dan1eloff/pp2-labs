# Classes
 
# 1
class toUpper:
    def __init__(self):
        self.text = ''
 
    def getString(self):
        self.text = str(input('Enter a string: '))
   
    def printString(self):
        print(self.text.upper())
 
# obj = toUpper()
# obj.getString()
# obj.printString()
 
# 2    
class Shape:
    def area(self):
        return 0
 
class Square(Shape):
    def __init__(self, length):
        self.length = length
 
    def area(self):
        return self.length ** 2
   
# shape = Shape()
# print("Default Shape Area:", shape.area())
 
# square = Square(5)
# print("Square Area:", square.area())