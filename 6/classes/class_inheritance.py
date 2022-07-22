# Сделать класс прямоугольник и треугольник

class Polygon:
    def is_valid(self):
        for x in self.sides:
            if x == 0:
                return False
        return True

    def perimenter(self):
        return sum(self.sides)

    def square(self):
        raise NotImplemented


class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.sides = [a, b, c]

    def perimenter(self):
        return 777


class Rectangle(Polygon):
    def __init__(self, a, b, c, d):
        self.sides = [a, b, c, d]

    def square(self):
        return self.sides[0] * self.sides[1]


class Pentagon(Polygon):
    def __init__(self, a, b, c, d, e):
        self.sides = [a, b, c, d, e]


tri = Triangle(3, 4, 5)
if tri.is_valid():
    print(tri.perimenter())


rect = Rectangle(1, 1, 1, 1)
if rect.is_valid():
    print("rect is ok")
    print(rect.square())

pent = Pentagon(1, 1, 2, 3, 4)
if pent.is_valid():
    print("pent is ok")
