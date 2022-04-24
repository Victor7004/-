# Напишите программу для вычисления суммы двух матриц.

n, m = [int(i)for i in input().split()]
mat1 = []
mat2 = []
for i in range(n):
    temp = [int(i)for i in input().split()]
    mat1.append(temp)
#print(mat1)
pusto = input()
for j in range(n):
    temp1 = [int(j)for j in input().split()]
    mat2.append(temp1)
#print(mat2)
s = 0
mat3 = [[0]*m for _ in range(n)]
#print(mat3)
for i in range(n):
    for j in range(m):
        mat3[i][j] = mat1[i][j] + mat2[i][j]
#print(mat3) 
for el in mat3:
    print(*el)
