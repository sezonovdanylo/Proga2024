from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

with open("input01.txt", "r") as file1:
    with open("input001.txt", "w") as file2:
        for el in file1:
            s = el.split()
            if len(s) == 2:
                s1 = QuadraticEquation(0, int(s[0]), int(s[1]))
            elif len(s) == 3:
                s1 = QuadraticEquation(int(s[0]), int(s[1]), int(s[2]))
            elif len(s) == 5:
                s1 = BiQuadraticEquation(int(s[0]), int(s[2]), int(s[4]))
            else:
                break

            file2.write((str(s1.solve())))
            file2.write('\n')
with open("input02.txt", "r") as file1:
    with open("input002.txt", "w") as file2:
        for el in file1:
            s = el.split()
            if len(s) == 2:
                s1 = QuadraticEquation(0, int(s[0]), int(s[1]))
            elif len(s) == 3:
                s1 = QuadraticEquation(int(s[0]), int(s[1]), int(s[2]))
            elif len(s) == 5:
                s1 = BiQuadraticEquation(int(s[0]), int(s[2]), int(s[4]))
            else:
                break

            file2.write((str(s1.solve())))
            file2.write('\n')

with open("input03.txt", "r") as file1:
    with open("input003.txt", "w") as file2:
        for el in file1:
            s = el.split()
            if len(s) == 2:
                s1 = QuadraticEquation(0, int(s[0]), int(s[1]))
            elif len(s) == 3:
                s1 = QuadraticEquation(int(s[0]), int(s[1]), int(s[2]))
            elif len(s) == 5:
                s1 = BiQuadraticEquation(int(s[0]), int(s[2]), int(s[4]))
            else:
                break

            file2.write((str(s1.solve())))
            file2.write('\n')




