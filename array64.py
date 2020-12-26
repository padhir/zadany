from random import randint
Na = int(input("Na ="))
Nb = int(input("Nb ="))
Nc = int(input("Nc ="))

D=[]

A = [randint(-10,10) for i in range(Na)]
B = [randint(-10,10) for i in range(Nb)]
C = [randint(-10,10) for i in range(Nc)]

print("A =",A, "B =",B,"C =",C)

A = sorted(A,reverse=True)
B = sorted(B,reverse=True)
C = sorted(C,reverse=True)
print("По убыванию: ","A =",A,"B =",B,"C =",C)

D = sorted( A + B + C, reverse=True)
print("D =",D)

