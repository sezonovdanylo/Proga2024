from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):

    def solve(self):
        solutions_of_quad = super().solve()
        if solutions_of_quad == BiQuadraticEquation.INF:
            return QuadraticEquation.INF
        result = set()
        for sol in solutions_of_quad:
            if float(sol) <0:
                continue
            else:
                result.add(sol**0.5)
                result.add(-sol**0.5)
        return tuple(result)

if __name__ == '__main__':
    eq1 = BiQuadraticEquation(2, 3, 4)
    print(eq1.solve())
    eq2 = BiQuadraticEquation(0, 5, 3)
    print(eq2.solve())
    eq3 = BiQuadraticEquation(5, 0, 0)
    print(eq3.solve())
    eq4 = BiQuadraticEquation(0, 0, 4)
    print(eq4.solve())
