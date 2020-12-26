import random
M = int(input("M ="))

A = [[random.randrange(10) for i in range(M)] for j in range(M)]
print(A)

for i in range(len(A)):
      print([0 for l in range(i)] + A[i][i:])

