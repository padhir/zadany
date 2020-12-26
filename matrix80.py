import random
M = int(input("M ="))

matr = [[random.randrange(10) for i in range(M)] for j in range(M)]
print(matr)
summ = 0
for i in range(1,M):
    summ += matr[i][i]
print(summ)
