from Figure import Figureseven
from random import randint



class Matrics():
    def __init__(self):
        self.zeromatrics = [[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]]
        self.matrics = [[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]]
        self.notfallenmatrics = [[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]]
        self.fallenfigure = [0]
        self.score = 0
        self.end = False
        self.centralfigure = 0
    def randomcreate(self):
        n = [randint(1, 9) / 10, randint(1, 9) / 10, randint(1, 9) / 10]
        number = randint(0, 6)
        randomfigure = Figureseven(n,number)
        self.create(randomfigure)
    def create(self, figure):

        self.centralfigure = figure
        self.placing()

    def placing(self):
        self.fakematrics = [[0,0],[0,0],[0,0],[0,0]]
        change = 0
        for i in range(0, 4):
            x = self.centralfigure.coordinats[i][0] - 1
            y = self.centralfigure.coordinats[i][1] + 2 + self.centralfigure.mooved
            self.centralfigure.matricscoordinats[i] = [x, y]
            self.fakematrics[i] = [x, y]
            if y<0:
                change = -1
            if y>9:
                change = 1
        if change == -1:
            self.centralfigure.mooved += 1
            self.placing()
        if change == 1:
            self.centralfigure.mooved -= 1
            self.placing()
        else:
            for el in self.fakematrics:
                self.matrics[el[0]][el[1]] = [self.centralfigure.color]

    def ochistka(self):
        for i in range(0,4):
            for k in range(0,10):
                self.matrics[i][k]=[0]
    def ifempty(self):
        empty = True
        for i in range(0,4):
            for k in range(0,10):
                if self.matrics[i][k]!=[0]:
                    empty=False
        return empty
    def centralpovorot(self):
        if self.centralfigure!=0:
            self.centralfigure.povorot()
            self.ochistka()
            self.placing()

    def left(self):
        if self.centralfigure != 0:
            self.centralfigure.left()
            self.ochistka()
            self.placing()

    def right(self):
        if self.centralfigure != 0:
            self.centralfigure.right()
            self.ochistka()
            self.placing()
    def figurefall(self):
        if self.fallenfigure == [0] and self.centralfigure!=0:
            coordinatslst = []
            colorlst = []
            for coordinats in self.centralfigure.matricscoordinats:
                coordinatslst.append(coordinats)
            for color in self.centralfigure.color:
                colorlst.append(color)
            self.fallenfigure = [coordinatslst, colorlst]
            self.centralfigure = 0


    def fall(self):
        if self.fallenfigure != [0]:
            k = []
            coordinats = self.fallenfigure[0]
            color = self.fallenfigure[1]
            fdc = coordinats
            fcc = []
            stopfigure = False
            for cord in coordinats:
                x = cord[0]+1
                y = cord[1]
                fcc.append([x,y])

                if x > 23:
                    stopfigure = True
                elif self.notfallenmatrics[x][y] != [0]:
                    stopfigure = True
            if stopfigure:
                for cordi in coordinats:
                    self.notfallenmatrics[cordi[0]][cordi[1]] = [color]
                    if cordi[0]<4:
                        self.end = True
                self.fallenfigure=[0]
            else:
                for el in fdc:
                    self.matrics[el[0]][el[1]] = [0]
                for ell in fcc:
                    self.matrics[ell[0]][ell[1]] = [color]
                self.fallenfigure[0] = fcc

    def notfallenfall(self, number):
        for row in range(number, -1, -1):
            for value in range(0,10):
                k = []
                if self.notfallenmatrics[row][value] != [0]:

                    for element in self.notfallenmatrics[row][value]:
                        k.append(element)
                    self.notfallenmatrics[row+1][value] = k
                    self.matrics[row+1][value] = k
                    self.notfallenmatrics[row][value] = [0]
                    self.matrics[row][value] = [0]


    def iffullrow(self):
        for row in range(23, -1, -1):
            scalerow = True
            for el in self.notfallenmatrics[row]:
                if el == [0]:
                    scalerow = False
            if scalerow:
                self.notfallenmatrics[row] = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
                self.matrics[row] = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
                self.notfallenfall(row)
                return True

    def endgame(self):
        if self.end:

            self.fallenfigure = [0]
            for row in range(0, 24):
                for value in range(0,10):
                    self.matrics[row][value] = [0]
                    self.notfallenmatrics[row][value] = [0]
            self.end = False












