# Напишите программу, которая меняет местами столбцы в матрице.

# На вход программе на разных строках подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа ii и jj — номера столбцов, подлежащих обмену
n, m = int(input()), int(input())

#i = int(ij[0])
#j = int(ij[1])
#2) Считываем номера столбцов как массив (список)
#3)колонка 1 = инт (массив из пункта 2[ ][ ]) в квадратных скобках индексы первого числа.
#4) Аналогично для второй колонки, только индекс второго числа в массиве
mat = [[int(i) for i in input().split()]for _ in range(n)]
#print(mat)
col = [int(_) for _ in input().split()] # '0 1'
#print(col)
col1=int(col[0])
col2=int(col[1])
#print(col1, col2)

for k in range(n):
    mat[k][col1], mat[k][col2] = mat[k][col2], mat[k][col1]
for i in range(len(mat)):
    for k in range(len(mat[i])):
        print(mat[i][k], end=' ')
    print()   
