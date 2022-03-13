# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.
n, m = input().split()
matrix = [[i for i in ('.' * int(m))]for i in range(int(n))]
count = 0
for i in range(int(m)):
    for j in range(int(n)):
        count +=1
        matrix[j][i] = count
for el in matrix:
    print(*el)

# Верное решение #471563515
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for j in range(m):
    for i in range(n):
        matrix[i][j] = j * n + i + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()    
