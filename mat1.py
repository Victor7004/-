# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n заполнив её в соответствии с образцом.
n = int(input())
mat = [[i for i in ([0]*n) ]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i + j + 1 == n or i == j:
            mat[i][j] = 1
for el in mat:
    print(*el)
