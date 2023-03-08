class Figure:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f'Я - класс {self.__class__}'

    def perimeter(self):
        return sum(self.args)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return sum((self.a, self.b, self.c))

    def area(self):
        return self.a * self.b / 2


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return self.a * 4

    def area(self):
        return self.a ** 2





f = Figure(1, 2, 3)
print(f)

t = Triangle(1, 2, 3)
print(t)
print(t.perimeter())
print(t.area())

r = Rectangle(2, 2)
print(r)
print(r.area())
print(r.perimeter())

s = Square(5)
print(s)
print(s.area())
print(s.perimeter())