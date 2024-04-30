class Segment:
    def __init__(self, x , y, T, F):
        self.x = x
        self.y = y
        self.LD = T
        self.RD = F


    def empty(self):
        return self.x > self.y or (self.x == self.y and (self.LD == False or self.RD == False))

    def __str__(self):
        if self.empty():
            return "Empty"
        if self.LD:
            LD = "["
        else:
            LD = "("
        if self.RD:
            RD = "]"
        else:
            RD = ")"
        return f"{LD} {self.x}, {self.y} {RD}"

    def __add__(self, other):
        if self.empty():
            return other
        if other.empty():
            return self


        if self.x < other.x:
            NewLN = self.x
            LD = self.LD
        elif other.x < self.x:
            NewLN = other.x
            LD = other.LD
        else:
            NewLN = self.x
            LD = self.LD or other.LD

        if self.y > other.y:
            NewRN = self.y
            RD = self.RD
        elif other.y > self.y:
            NewRN = other.y
            RD = other.RD
        else:
            NewRN = self.y
            RD = self.RD or other.RD

        return Segment(NewLN, NewRN, LD, RD)

class SegmentSet():
    def __init__(self, lst):
        self.lst = lst
    def __add__(self, other):
        lst = self.lst
        lst2 = []
        for i in range(0, len(lst), 2):
            if not lst[i].y<=lst[i+1].x:
                lst2.append(lst[i]+lst[i+1])
            else:
                












a = Segment(2, 3, True, False)
b = Segment(3, 4, True, False)
print(a+b)




