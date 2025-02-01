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

# 3
class Rectangle(Shape):
    def __init__(self,  lenght, widht):
        self.length = lenght
        self.widht = widht
    
    def area(self):
        return self.length * self.widht

# abcd = Rectangle(5,4)
# print(abcd.area())

# 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        text = 'Coordinates of the specified point: ('+str(self.x)+';'+str(self.y)+')'
        return text
    
    def move(self, plus_x, plus_y):
        self.x += plus_x
        self.y += plus_y
        
        text = 'Now the coordinates of the specified point: ('+str(self.x)+';'+str(self.y)+')'
        return text
    
    def dist(self):
        text = 'Distance between x and y: ' + str((self.x**2 + self.y**2)**0.5)
        return text

# to4ka = Point(5,10)
# print(to4ka.show())
# print(to4ka.move(5,15))
# print(to4ka.show())
# print(to4ka.dist())