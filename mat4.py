# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "змейкой" в соответствии с образцом.
n, m = [int(i)for i in input().split()]
mat = [[0]*m for _ in range(n)]
count = 1
for i in range(n):
    for j in range(m):
        mat[i][j] = count
        count += 1
for i in range(n):
    if i%2!=0:
        mat[i] = mat[i][::-1]           
for el in mat:
    print(*el)

# Верное решение #474082930
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
    if i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()    
