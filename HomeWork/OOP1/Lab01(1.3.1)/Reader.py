from figures import Triangle
from figures import Rectangle
from figures import Trapeze
from figures import Parallelogram
from figures import Circle

class FReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        fig=[]
        with open(self.file_name) as f:
            for line in f:
                lst = line.split()
                if lst[0]=="Triangle":
                    a, b, c = float(lst[-3]), float(lst[-2]), float(lst[-1])
                    fi= Triangle(a, b, c)
                    fig.append(fi)
                if lst[0]=="Rectangle":
                    a, b = float(lst[-2]), float(lst[-1])
                    fi= Rectangle(a, b)
                    fig.append(fi)
                if lst[0]=="Trapeze":
                    a, b, c, d = float(lst[-4]), float(lst[-3]), float(lst[-2]), float(lst[-1])
                    fi= Trapeze(a, b, c, d)
                    fig.append(fi)
                if lst[0] == "Parallelogram":
                    a, b, h = float(lst[-3]), float(lst[-2]), float(lst[-1])
                    fi = Parallelogram(a, b, h)
                    fig.append(fi)
                if lst[0] == "Circle":
                    r = float(lst[-1])
                    fi = Circle(r)
                    fig.append(fi)
        return fig

def readme(txt):
    reader = FReader(txt)
    F = reader.read()
    P=0
    S=0
    k=0
    for n in F:
        p = n.Per()
        s = n.Plo()
        if p>P:
            P=p
        if s>S:
            S=s
    for n in F:
        p = n.Per()
        s = n.Plo()
        if p==P and s ==S:
            print("Perimetr:", p, "Ploshad:", s, "Figure:", n.who(), n)
            k=1
    if k==0:
        print("This figure does not exist")