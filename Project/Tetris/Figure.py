from random import randint



class Figure:
    def __init__(self, a, n):
        self.coordinats = a
        self.color = n
        self.active = 0


    def povorotFIGURE(self):
        a = self.coordinats
        for i in range(0, 4):
            x = self.coordinats[i][0]
            y = self.coordinats[i][1]
            self.coordinats[i][0], self.coordinats[i][1] = y, 5-x
        return(Figure(self.coordinats, self.color))

    def povorotLST(self, lst):
        r = []
        for el in lst:
            x = el[0]
            y = el[1]
            r.append([y, 5 - x])
        return r


class Figureseven(Figure):
    def __init__(self, color, number):
        self.color = color
        self.mooved = 0
        f1 = [[4, 2], [3, 2], [3, 3], [4, 3]]
        f2 = [[4, 1], [4, 2], [4, 3], [3, 2]]
        f3 = [[4, 1], [4, 2], [3, 2], [3, 3]]
        f4 = [[3, 2], [3, 3], [4, 3], [4, 4]]
        f5 = [[3, 2], [4, 2], [4, 3], [4, 4]]
        f6 = [[3, 3], [4, 3], [4, 2], [4, 1]]
        f7 = [[4, 1], [4, 2], [4, 3], [4, 4]]
        figures = [f1, f2, f3, f4, f5, f6, f7]
        pochatok = figures[number]
        self.gradius0= pochatok
        a = pochatok
        b = self.povorotLST(a)
        c = self.povorotLST(b)
        d = self.povorotLST(c)
        self.gradiuslst = [a, b, c, d]
        self.numberlst = 0
        self.coordinats = pochatok
        self.matricscoordinats=[[0,0], [0,0], [0,0], [0,0]]
        # self.futurematricscoordinats=[[0,0], [0,0], [0,0], [0,0]]


    def left(self):
        self.mooved -=1
    def right(self):
        self.mooved +=1
    def povorot(self):
        self.numberlst += 1
        if self.numberlst == 4:
            self.numberlst = 0
        self.coordinats = self.gradiuslst[self.numberlst]






