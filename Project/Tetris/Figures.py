from Figure import Figure
from random import randint



f1 = [[4,2],[3,2],[3,3],[4,3]]
f2 = [[4,1],[4,2],[4,3],[3,2]]
f3 = [[4,1],[4,2],[3,2],[3,3]]
f4 = [[3,2],[3,3],[4,3],[4,4]]
f5 = [[3,2],[4,2],[4,3],[4,4]]
f6 = [[3,3],[4,3],[4,2],[4,1]]
f7 = [[4,1],[4,2],[4,3],[4,4]]


figures = [f1, f2, f3, f4, f5, f6, f7]

class Matrics():
    def __init__(self):
        self.matrics = [[[0,0]]*10]*24
    def create(self, figure):
        self.centralfigure = figure
        for el in self.centralfigure.coordinats:
            x = el[0]
            y = el[1]
            self.matrics[x-1][y+2]=[1,self.centralfigure.color]
    def ochistka(self):
        for a in range (0,4):
            for b in range(0,10):
                self.matrics[a][b] = [0,0]
    def centralpovorot(self):
        self.ochistka()
        self.create(figure.povorot())


Matrics = Matrics()
figure = Figure(f7, 5)

print(Matrics.matrics)
Matrics.create(figure)
print(Matrics.centralfigure.coordinats)
print(Matrics.matrics)



Matrics.centralpovorot()
print(Matrics.centralfigure.coordinats)
print(Matrics.matrics)


Matrics.ochistka()
print(Matrics.matrics[3][4])