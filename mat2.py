# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её в соответствии с образцом.
n = int(input())
mat = [[i for i in ([0]*n)]for _ in range(n)] 
for i in range(n):
    for j in range(n):
        if i == j or j + i + 1 == n:
            mat[i][j] = 1
        if i < 1 or i == n - 1:
            mat[i][j] = 1
        if i < j and i < n - 1 - j:
            mat[i][j] = 1
        if i > j and i > n - 1 - j:
            mat[i][j] = 1
for el in mat:
    print(*el)
