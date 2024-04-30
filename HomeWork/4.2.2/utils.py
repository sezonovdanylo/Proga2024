def fact(n):
    if n!=1:
        return n*fact(n-1)
    else:
        return 1

def pure(n):
    for i in range(3, int(n**0.5+2)):
        if n%i==0:
            return False
    return True

def five(n):
    if n!=5:
        if n<5:
            return False
        return five(n/5)
    else:
        return True

def two(n):
    if n!=2:
        if n<2:
            return False
        return two(n/2)
    else:
        return True