from random import randint
N = int(input("N ="))
K = int(input("K ="))

nabor = [[randint(-10,10) for i in range(N)] for j in range(K)]
print(nabor)

a = [x for xs in nabor for x in xs]
print(a)

summ = 0
for i in a:
    summ += i
print(summ)
