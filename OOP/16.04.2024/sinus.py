from math import *
def sinus(x):
    e = 1/10**10
    S0 = x
    a0 = x
    i=1
    yield S0
    while True:
        s0 = S0
        a0 = (-a0*x**2)/(2*i*(2*i+1))
        S0 = S0+a0
        yield S0
        if abs(S0 - s0) <e:
            break
        i+=1
for el in sinus(pi/6):
    print(el)
print(sin(pi/6))




