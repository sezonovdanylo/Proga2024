def drib1(x):
    x0 = 1
    for i in range(1, x+1):
        x0 = 1+ 1/x0
    return x0
print(drib1(10), drib1(24))

def drib2(x):
    x0 = 1
    x1 = 1+ 1/2
    for i in range(2, x+1):
        xn = 1 + 1/(2+(x1 - 1))
        x1 = xn
    return x1
print(drib2(10))
def driub3(x):
    x0 = 1
    x1 = 2 + 1/2
    for i in range(2, x+1):
        xn = 2 + 1/x1
        x1 = xn
    return x1-1
print(driub3(10))


def stepen(x):
    x0= "1"
    a = 1
    while True:
        a = a*10
        x0 = x0+str(a)
        if len(x0)>x:
            break
    return(x0[x-1], x0)
print(stepen(7))

def stepen1(x):
    x0= 1
    a = 1
    while True:
        a = a*10
        x0 = x0*a*10+a
        if len(x0)>x:
            break
    return(x0[x-1], x0)
print(stepen(8))

def pidryad(x):
    pos1 = 0
    i = 1
    while True:
        pos1 = pos1 + i
        i+=1
        if pos1 >=x-1:
            break
    if pos1 == x-1:
        return 1
    else:
        return 0
print(pidryad(100))








