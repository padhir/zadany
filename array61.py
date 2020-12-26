from random import randint
n = int(input("n ="))

a = []
b = []
for i in range(n):
    a.append(randint(-10, 10))
print(a)

summ = 0
for i in range(n-1,-1,-1):
    summ += a[i]/n
    b.insert(0,summ)
print(b)
    
