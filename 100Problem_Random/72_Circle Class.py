import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        return 2 * math.pi * self.radius
    
circle = Circle(5.00)

print(circle.area())
print(circle.circumference())