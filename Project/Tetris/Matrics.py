from Figure import Figure, Figureseven
from random import randint



class Matrics():
    def __init__(self):
        self.zeromatrics = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
        self.matrics = self.zeromatrics
        self.fallenfigures=[]
        self.score=0
        self.end=False
    def randomcreate(self):
        n = [randint(1, 9) / 10, randint(1, 9) / 10, randint(1, 9) / 10]
        number = randint(0, 6)
        randomfigure = Figureseven(n,number)
        self.create(randomfigure)
    def create(self, figure):

        self.centralfigure = figure
        self.placing()
    def placing(self):
        fig = self.centralfigure
        self.fakematrics = []


        for el in self.centralfigure.coordinats:
            x = el[0] - 1
            y = el[1] + 2
            self.centralfigure.matricscoordinats.append([x,y])
            x = x
            y = y+fig.mooved

            self.fakematrics.append([x,y])
            if y<0:
                self.centralfigure.right()
                self.placing()
            elif y>9:
                self.centralfigure.left()
                self.placing()
            else:
                for el in self.fakematrics:
                    self.matrics[el[0]][el[1]] = [0, fig.color]

    def ochistka(self):
        for i in range(0,4):
            for k in range(0,9):
                self.matrics[i][k]=[0,0]
    def ifempty(self):
        empty = True
        for i in range(0,4):
            for k in range(0,9):
                if self.matrics[i][k]!=[0,0]:
                    empty=False
        return empty


    def centralpovorot(self):
        self.centralfigure.povorot()
        self.ochistka()
        self.create(self.centralfigure)

    def left(self):
        self.centralfigure.left()
        self.ochistka()
        self.create(self.centralfigure)

    def right(self):
        self.centralfigure.right()
        self.ochistka()
        self.create(self.centralfigure)
    def figurefall(self):
        self.fallenfigures.append(self.centralfigure)

    def fall(self):

        for fig in range(0,len(self.fallenfigures)):
            fdc = []                                           #Future Delete Coordinats
            fcc = []                                           #Future Change Coordinats
            color = self.fallenfigures[fig].color
            stopfigure = False
            for i in range(0,4):
                fdc.append(self.fallenfigures[fig].matricscoordinats[i])
                self.fallenfigures[fig].matricscoordinats[i][0]+=1
                if self.fallenfigures[fig].matricscoordinats[i][0]>23:
                    stopfigure = True
                elif self.matrics[self.fallenfigures[fig].matricscoordinats[i][0]][self.fallenfigures[fig].matricscoordinats[i][1]]!=[0,0]:
                    stopfigure = True
                    if stopfigure:
                        if fdc[i][0]<4:
                            self.end=True
                fcc.append(self.fallenfigures[fig].matricscoordinats[i])
            if stopfigure:
                del self.fallenfigures[fig]
            else:
                for delcoordinats in fdc:
                    self.matrics[delcoordinats[0]][delcoordinats[1]]=[0,0]
                for chncoordinats in fcc:
                    self.matrics[chncoordinats[0]][chncoordinats[1]]=[0,color]
    def iffullrow(self):
        pass
    def endgame(self):
        pass








