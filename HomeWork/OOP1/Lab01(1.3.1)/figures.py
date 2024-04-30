from math import pi


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def Per(self):
        if self.a or self.b or self.c < 0:
            return 0
        return (self.a + self.b + self.c)
    def Plo(self):
        p=(self.a + self.b + self.c)/2
        if self.a or self.b or self.c <= 0:
            return 0
        return ((p*(p-self.a)*(p-self.b)*(p-self.c))**0.5)
    def who(self):
        return ("Triangle:", self.a, self.b, self.c)



class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Per(self):
        if self.a or self.b < 0:
            return 0
        return (2*self.a + 2*self.b)
    def Plo(self):
        if self.a or self.b <= 0:
            return 0
        return (self.a * self.b)
    def who(self):
        return ("Rectangle:", self.a, self.b)


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def Per(self):
        if self.a or self.b or self.c or self.d < 0:
            return 0
        return (self.a + self.b + self.c + self.d)
    def Plo(self):
        if self.a or self.b or self.c or self.d <= 0:
            return 0
        m = ((self.a - self.b)**2 + self.c**2 - self.d**2)/(2*(self.a - self.b))
        h = (self.c**2 - m**2)**0.5
        return ((self.a + self.b)*h/2)
    def who(self):
        return ("Trapeze:", self.a, self.b, self.c, self.d)


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def Per(self):
        if self.a or self.b or self.h < 0:
            return 0
        return (2 * self.a + 2 * self.b)
    def Plo(self):
        if self.a or self.b or self.h <= 0:
            return 0
        return (self.a * self.h)
    def who(self):
        return ("Parallelogram:", self.a, self.b, self.h)



class Circle:
    def __init__(self, r):
        self.r = r
    def Per(self):
        if self.r < 0:
            return 0
        return (2*pi*self.r)
    def Plo(self):
        if self.r <= 0:
            return 0
        return (pi * self.r * self.r)
    def who(self):
        return ("Circle:", self.r)