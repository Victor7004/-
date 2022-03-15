# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.
n, m = [int(i)for i in input().split()]
mat = [[0]*m for _ in range(n)]
mat1 = []
count = 1
for i in range(1, m+1):
    mat1.append(count)
    count += 1   
for i in range(n):
    if i > m:
        mat[i] = mat1[i % m :]+mat1[:i % m]
    else:
        mat[i] = mat1[i:]+mat1[:i]
for el in mat:
    print(*el)
    
# Верное решение #469419213
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1
          
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()    
