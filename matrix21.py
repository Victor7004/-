# На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n и заполняет её по следующему правилу:

# числа на побочной диагонали равны 1;
# числа, стоящие выше этой диагонали, равны 0;
# числа, стоящие ниже этой диагонали, равны 2.

n = int(input())
matrix = [[i for i in (' ' * n)]for _ in range(n)]
#print(matrix)
for i in range(n):
    for j in range(n):
        if i + j + 1 < n:
            matrix[i][j] = 0
        if i + j + 1 > n:
            matrix[i][j] = 2
        if i + j + 1 == n:
            matrix[i][j] = 1
for el in matrix:
    print(*el)
