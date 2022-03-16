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
