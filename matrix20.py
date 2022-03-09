# На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n \times mn×m, заполнив её символами . и * в шахматном порядке.
# В левом верхнем углу должна стоять точка.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.
n, m = input().split()
matrix = [[i for i in ('.'*int(m))] for i in range(int(n))]  
for i in range(int(n)):
    for j in range(int(m)):
        if (i+j) % 2 == 0:
            matrix[i][j]='.'
        else:    
            matrix[i][j]='*'
for el in matrix:
    print(*el)
# Sample Output    
# . * . *
# * . * .
# . * . *
