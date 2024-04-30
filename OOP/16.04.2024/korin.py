def korin(x, k):
    x0 = x/k
    x1 = 1 / k * ((k - 1) * x0 + x / (x0 ** (k - 1)))
    e=0.000000000000000001
    while True:
        x0 = x1
        x1 = 1/k*((k-1)*x1 + x/(x1**(k-1)))
        if abs(x1 - x0)<e:
            return x1
print(korin(625, 4))

