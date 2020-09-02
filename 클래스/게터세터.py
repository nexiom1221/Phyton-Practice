import math

class Circle:
    def __init__(self, radious):
        self.__radious = radious
    
    def get_circumference(self):
        return 2 * math.pi * self.__radious
    
    def get_area(self):
        return math.pi * (self.__radious ** 2)
    
    def get_radious(self):
        return self.__radious
    
    def set_radious(self, value):
        self.__radious = value
    

circle = Circle(10)

print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

print("# __radious에 간접적으로 접근")
print(circle.get_radious())
print()

circle.set_radious(2)
print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

