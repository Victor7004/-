# Напишите программу, которая перемножает две матрицы.
n, m = [int(i)for i in input().split()]
A = []
B = []
for i in range(n):
    A1=[int(i)for i in input().split()]
    A.append(A1)
#print(A)
pusto = input()
m, k = [int(j)for j in input().split()]
for j in range(m):
    B1= [int(i)for i in input().split()]
    B.append(B1)
#print(B)
C = []
for _ in range(n):
    C.append ([0]*k)
#c=[] for _ in range(n): c.append([0]*k)
#print(C)
#x = 0
for i in range( n):
    for j in range(k):
        sum = 0
        for x in range(m):
            sum += A[i][x]*B[x][j]
        #x +=1
        C[i][j] = sum
#print(C)
for el in C:
    print(*el)

# Верное решение #469420019
n, m = [int(i) for i in input().split()]
matrixA = [[int(i) for i in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
matrixB = [[int(i) for i in input().split()] for _ in range(m)]
matrixC = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for q in range(m):
            matrixC[i][j] += matrixA[i][q] * matrixB[q][j]

for row in matrixC:
    print(*row)
