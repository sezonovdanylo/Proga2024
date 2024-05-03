from random import randint



class Figure:
    def __init__(self, a, n):
        self.coordinats = a
        self.color = n
        self.active = 1


    def povorot(self):
        a = self.coordinats
        for i in range(0, 4):
            x = self.coordinats[i][0]
            y = self.coordinats[i][1]
            self.coordinats[i][0], self.coordinats[i][1] = y, 5-x
        return(Figure(self.coordinats, self.color))

    def randomlist(self):
        f1 = [[4, 2], [3, 2], [3, 3], [4, 3]]
        f2 = [[4, 1], [4, 2], [4, 3], [3, 2]]
        f3 = [[4, 1], [4, 2], [3, 2], [3, 3]]
        f4 = [[3, 2], [3, 3], [4, 3], [4, 4]]
        f5 = [[3, 2], [4, 2], [4, 3], [4, 4]]
        f6 = [[3, 3], [4, 3], [4, 2], [4, 1]]
        f7 = [[4, 1], [4, 2], [4, 3], [4, 4]]

        n = [randint(1,9)/10, randint(1,9)/10, randint(1,9)/10]
        figures = [f1, f2, f3, f4, f5, f6, f7]

        # далі буде список з екземплярами класів фігур в яких буде однаковий рандомний попередньо вибраний колір, і буду брати рандом по цьомусписку
        return





if __name__ == '__main__':

    a = [[4,1], [4,2], [4,3], [3,2]]
    Fig = Figure(a, 5)
    print(Fig.povorot().coordinats)



