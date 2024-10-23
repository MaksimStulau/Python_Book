"""1. Создать классы: Point, Shape, Rectangular, Square, Triangular, Circle.
   Все классы наследуются от Shape, кроме Point.
   В классе Shape есть метод draw(), get_area(), get_perimeter, to_string().
   У Rectangular, Square, Triangular, Circle
   есть переопределенные методы get_perimeter, get_area(), to_string(), соотвествующие конструкторы.
   Классы также должны переопределять метод draw.

   - Создать класс Rectangular. У него есть длина, ширина, конструктор.
     Также есть методы get_area(), get_perimeter.
   - Создать класс Circle. У него есть радиус, конструктор. Также есть методы get_area(), get_perimeter.
   - Создать класс Point. У него есть x, y. Также есть метод get_distance_to(Point).
   - Создать класс Triangle. У него есть три точки. Также есть методы get_area(), get_perimeter.
   - Создать класс Square. У него есть сторона. Также есть методы get_area(), get_perimeter.
   - Добавить в конструктор Rectangular, Square, Сircle точку,
     добавить метод get_location - возвращает центр фигуры.
   - Создать класс Shape с методами draw(), get_area(), get_perimeter, to_string()
     и унаследовать все фигуры от него. Переопределить соотвествющие методы.
   - Для метода draw использовать модуль turtle (https://opentechschool.github.io/python-beginners/ru)"""


import math
import turtle


class Shape:
    def draw(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def to_string(self):
        return "Shape"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def to_string(self):
        return f"Point({self.x}, {self.y})"


class Rectangular(Shape):
    def __init__(self, length, width, center):
        self.length = length
        self.width = width
        self.center = center

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def draw(self):
        t = turtle.Turtle()

        # Перемещаемся к начальной точке
        t.penup()
        t.goto(self.center.x - self.length / 2, self.center.y - self.width / 2)
        t.pendown()

        # Рисуем прямоугольник
        for _ in range(2):
            t.forward(self.length)
            t.left(90)
            t.forward(self.width)
            t.left(90)

        turtle.done()

    def get_location(self):
        return self.center.to_string()

    def to_string(self):
        return f"Rectangular(length={self.length}, width={self.width}, center={self.center.to_string()})"


class Circle(Shape):
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def draw(self):
        t = turtle.Turtle()

        # Перемещаемся к началу рисования
        t.penup()
        t.goto(self.center.x, self.center.y - self.radius)
        t.pendown()

        # Рисуем круг
        t.circle(self.radius)

        turtle.done()

    def get_location(self):
        return self.center.to_string()

    def to_string(self):
        return f"Circle(radius={self.radius}, center={self.center.to_string()})"


class Square(Shape):
    def __init__(self, side, center):
        self.side = side
        self.center = center

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

    def draw(self):
        t = turtle.Turtle()

        # Перемещаемся к начальной точке
        t.penup()
        t.goto(self.center.x - self.side / 2, self.center.y - self.side / 2)
        t.pendown()

        # Рисуем квадрат
        for _ in range(4):
            t.forward(self.side)
            t.left(90)

        turtle.done()

    def get_location(self):
        return self.center.to_string()

    def to_string(self):
        return f"Square(side={self.side}, center={self.center.to_string()})"


class Triangular(Shape):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def get_area(self):
        a = self.p1.get_distance_to(self.p2)
        b = self.p2.get_distance_to(self.p3)
        c = self.p3.get_distance_to(self.p1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def get_perimeter(self):
        return (self.p1.get_distance_to(self.p2) +
                self.p2.get_distance_to(self.p3) +
                self.p3.get_distance_to(self.p1))

    def draw(self):
        t = turtle.Turtle()

        # Перемещаемся к первой точке
        t.penup()
        t.goto(self.p1.x, self.p1.y)
        t.pendown()

        # Рисуем треугольник
        t.goto(self.p2.x, self.p2.y)
        t.goto(self.p3.x, self.p3.y)
        t.goto(self.p1.x, self.p1.y)

        turtle.done()

    def to_string(self):
        return f"Triangular(p1={self.p1.to_string()}, p2={self.p2.to_string()}, p3={self.p3.to_string()})"


