# На вход программе подаются два натуральных числа nn и mm.
# Напишите программу, которая создает матрицу размером n \times mn×m и заполняет её числами от 11 до n \cdot mn⋅m в соответствии с образцом.
# На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

n, m = input().split()
matrix = [[i for i in ('.'*int(m))]for i in range(int(n))]
#print(matrix)
count = 0
for i in range(int(n)):
    for j in range(int(m)):
        count += 1
        matrix[i][j]=count
#print(matrix)        
for el in matrix:
    print (*el)
    
# Верное решение #432048897
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
