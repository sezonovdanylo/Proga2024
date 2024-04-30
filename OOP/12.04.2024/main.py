def triban(x):
    x0 = 0
    x1 = 1
    x2 = 1
    for i in range(3, x+1):
        x2, x1, x0 = x2+x0, x2, x1
    return x2
print(triban(24))
