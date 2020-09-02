import math

class Circle:
    def __init__(self, radious):
        self.__radious = radious
    
    def get_circumference(self):
        return 2 * math.pi * self.__radious
    
    def get_area(self):
        return math.pi * (self.__radious ** 2)

    
circle = Circle(10)

print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

print(circle.__radius)

