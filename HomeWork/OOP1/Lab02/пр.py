n = int(input())
a= 0
for i in range (1, n+1):
    a+= 2**(n-i) * i**2
print(a)