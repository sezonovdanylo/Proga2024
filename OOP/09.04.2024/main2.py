def summan():
    s = 1
    n = 1
    yield s, n
    while True:
        n +=1
        s += 1/n
        yield s, n

for S, n in summan():
    print(S, n)
    if S> 10:
        break