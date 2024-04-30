# a = 1
# n= 0
# e = 1/10**8
# while True:
#     n+=1
#     aprev = a
#     a = a + (-1)**n*1/(2*n +1)
#     if abs(a - aprev)<e:
#         break
# print(a*4, n)

def pipidrachunok():
    i = 2
    a = i**2/((i-1)*(i+1))
    e = 1/10**15
    while True:
        i+=2
        an = a
        a = a*i**2/((i-1)*(i+1))
        if abs(a - an)<e:
            return a*2, i/2-1
            break
print(pipidrachunok())


def dobutokpi():
    e = 1/10**15
    a = 0.5**0.5
    n = 0
    while True:
        n+=1
        a0 = a
        a = a*((0.5 + 0.5*a)**0.5)
        if abs(a - a0) < e:
            return 1/a*2, n
            break
print(dobutokpi())


