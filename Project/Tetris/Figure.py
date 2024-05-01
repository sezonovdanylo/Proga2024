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



if __name__ == '__main__':

    a = [[4,1], [4,2], [4,3], [3,2]]
    Fig = Figure(a, 5)
    print(Fig.povorot().coordinats)



