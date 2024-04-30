class Equation:
    INF = "infinity"
    def __init__(self, b, c):
        self.b = b
        self.c = c
    def solve(self):
        if self.b != 0 :
            x1 = -self.c/self.b
            return (x1,)
        else:
            if self.c == 0:
                return Equation.INF
            else:
                return ()

if __name__ == '__main__':
    eq1 = Equation(2, 3)
    print(eq1.solve())
    eq2 = Equation(0, 5)
    print(eq2.solve())
    eq3 = Equation(5, 0)
    print(eq3.solve())
    eq4 = Equation(0, 0)
    print(eq4.solve())