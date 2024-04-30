from math import *
def cosinus(x):
    e = 1 / 10 ** 10
    S0 = 1
    a0 = 1
    i = 0
    yield S0
    while True:
        i+=1
        a0 = (-a0 * x ** 2) / (2 * i * (2 * i - 1))
        S0 = S0 + a0
        yield S0
        if abs(a0) < e:
            break


for el in cosinus(pi / 6):
    print(el)
print(cos(pi / 6))