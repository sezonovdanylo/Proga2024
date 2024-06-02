from Matrics import Matrics

matrics = Matrics()
matrics.randomcreate()
print(matrics.matrics)
matrics.figurefall()
for i in range(0, 30):
    matrics.fall()
print(matrics.matrics)
matrics.notfallenfall(23)
