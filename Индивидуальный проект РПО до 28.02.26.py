from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r  # не через math.pi (упрощение)

    def diameter(self):
        return self.r * 2

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

class Triangle(Shape):

    def __init__(self, h, b):
        self.h = h
        self.b = b

    def area(self):
        return 0.5 * self.h * self.b

    def info(self):
        return "Простой треугольник"

circle = Circle(7)
rectangle = Rectangle(4, 8)
triangle = Triangle(6, 10)

print("Площадь круга:", circle.area())
print("Площадь прямоугольника:", rectangle.area())
print("Площадь треугольника:", triangle.area())
