from Figure import Figureseven
from random import randint



class Matrics():
    def __init__(self):
        self.zeromatrics = [[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]]
        self.matrics = [[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]]
        self.notfallenmatrics = [[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]]
        self.fallenfigures = []
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
            for k in range(0,9):
                self.matrics[i][k]=[0]
    def ifempty(self):
        empty = True
        for i in range(0,4):
            for k in range(0,9):
                if self.matrics[i][k]!=[0]:
                    empty=False
        return empty
    def centralpovorot(self):
        if self.centralfigure!=0:
            self.centralfigure.povorot()
            self.ochistka()
            self.create(self.centralfigure)

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
        coordinatslst = []
        colorlst = []
        for coordinats in self.centralfigure.matricscoordinats:
            coordinatslst.append(coordinats)
        for color in self.centralfigure.color:
            colorlst.append(color)
        self.fallenfigures.append([coordinatslst, colorlst])
        self.centralfigure = 0


    def fall(self):
        for i in range(0, len(self.fallenfigures)):
            coordinats = self.fallenfigures[i][0]
            color = self.fallenfigures[i][1]
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
                self.fallenfigures.pop(i)
            else:
                for el in fdc:
                    self.matrics[el[0]][el[1]] = [0]
                for ell in fcc:
                    self.matrics[ell[0]][ell[1]] = [color]
                self.fallenfigures[i][0] = fcc

    def notfallenfall(self, number):
        self.notfallenmatrics[number] = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
        for row in range(0, number):
            for el in range(0,10):
                if self.notfallenmatrics[row][el] != [0]:
                    for k in self.notfallenmatrics[row][el]:
                        self.notfallenmatrics[row+1][el] = k
                        self.matrics[row+1][el] = k
                        self.notfallenmatrics[row][el] = [0]
                        self.matrics[row][el] = [0]


    def iffullrow(self):
        for row in range(23, -1, -1):
            scalerow = True
            for el in self.notfallenmatrics[row]:
                if el == [0]:
                    scalerow = False
            if scalerow:
                self.notfallenfall(row)
                self.iffullrow()



    def endgame(self):
        pass







