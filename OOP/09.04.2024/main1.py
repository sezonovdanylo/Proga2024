def gen(n, x):
    a = x
    yield a

    for k in range(1, n+1):
        a = -x**2/(2*k*(2*k+1)) * a
    yield a

n = int(input("n = "))
x = float(input("x = "))

for el in gen(n, x):
    print(el)