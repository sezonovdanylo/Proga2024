from random import randint
from turtle import *
from math import radians, sin, cos, pi
r = randint

class Triangle:

    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)   # абсолютна позиція першої вершини
        self.vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.vertex2 = (x2, y2)  # позиція третьої відносно першої вершини
        self.color = "black"     # колір трикутника за промовчанням
        self.position1 = (self.position[0] + self.vertex1[0], self.position[1] + self.vertex1[1])
        self.position2 = (self.position[0] + self.vertex2[0], self.position[1] + self.vertex2[1])

    def set_position(self, x, y):
        self.position = (x, y)
        self.position1 = (self.position[0] + self.vertex1[0], self.position[1] + self.vertex1[1])
        self.position2 = (self.position[0] + self.vertex2[0], self.position[1] + self.vertex2[1])

    def set_color(self, color):
        self.color = color
    def paint(self):
        up()
        speed(100)
        pencolor(self.color)
        setpos(self.position)
        down()
        goto(self.position1)
        goto(self.position2)
        goto(self.position)

    def set_rotation(self, rotation):  # значення в радіанах
        self.rotation = rotation
        a1 = self.position1[0]
        b1 = self.position1[1]
        a2 = self.position2[0]
        b2 = self.position2[1]
        sfi = sin(rotation)
        cfi = cos(rotation)

        self.position1 = (cfi*a1 - sfi*b1, sfi*a1 + cfi*b1)
        self.position2 = (cfi * a2 - sfi * b2, sfi * a2 + cfi * b2)

    def set_scale(self, scale_x, scale_y):  # значення розтягу
        # по осях x та y відподно
        self.scale = (scale_x, scale_y)



def Drawing(num):
    TheTriangles=[]
    for i in range(num):
        triangle = Triangle(r(-200, 200), r(-200, 200), r(-200, 200), r(-200, 200))
        TheTriangles.append(triangle)
    for el in TheTriangles:
        el.set_position(r(-200, 200), r(-200, 200))
        el.set_color((r(0, 10) / 10, r(0, 10) / 10, r(0, 10) / 10))
        el.paint()
    mainloop()

# def animation(rad):
#     for i in range(1080//rad):








