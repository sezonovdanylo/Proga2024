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
        self.matrics = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

    def create(self, figure):
        self.centralfigure = figure
        self.coordinats = []
        for el in self.centralfigure.coordinats:
            x = el[0]
            y = el[1]
            self.matrics[x-1][y+2]=[0,self.centralfigure.color]
            self.coordinats.append([x-1,y+2])
    def ochistka(self):
        for a in range (0,4):
            for b in range(0,10):
                self.matrics[a][b] = [0,0]
    def centralpovorot(self):
        self.ochistka()
        self.create(self.centralfigure.povorot())
    def left(self):
        leftcoordinats=[]
        a=0
        for el in self.coordinats:
            x=el[0]
            y=el[1]-1
            leftcoordinats.append([x,y])
            if y<0:
                break
            a+=1
        if a==4:
            self.coordinats=leftcoordinats



    def right(self):
        rightcoordinats = []
        a = 0
        for el in self.coordinats:
            x = el[0]
            y = el[1]+1
            rightcoordinats.append([x, y])
            if y > 9:
                break
            a += 1
        if a == 4:
            self.coordinats = rightcoordinats





Matrics = Matrics()
figure = Figure(f7, 5)

print(Matrics.matrics)
Matrics.create(figure)
print(Matrics.centralfigure.coordinats)
print(Matrics.matrics)
print(Matrics.coordinats)



Matrics.centralpovorot()
print(Matrics.centralfigure.coordinats)
print(Matrics.matrics)
print(Matrics.coordinats)

for i in range(4):
    Matrics.left()
    print(Matrics.coordinats)
for i in range(11):
    Matrics.right()
    print(Matrics.coordinats)
#
#
# Matrics.ochistka()
# print(Matrics.matrics[3][5])