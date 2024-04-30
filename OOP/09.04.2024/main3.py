def viznachnik(x):
    D1 = 5
    D2 = 19
    for i in range (3, x+1):
        D2, D1 = 5* D2 - 6 *D1, D2
    return D2
print(viznachnik(7))
