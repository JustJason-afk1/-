import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


v1 = Vector2D(3, 4)
v2 = Vector2D(1, -2)

print("Сложение:")
print(v1 + v2)

print("\nВычитание:")
print(v1 - v2)

print("\nДлина вектора:")
print(v1.length())

print("\nСтроковое представление:")
print(v1)
