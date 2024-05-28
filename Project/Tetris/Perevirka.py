# from Matrics import Matrics


class Perevirka():
    def __init__(self):
        self.a = [1]
        self.b = []
    def abe(self):
        for el in self.a:
            self.b.append(el)

        self.a[0]=5
perev = Perevirka()
perev.abe()

print(perev.a, perev.b)