# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

n = int(input())
mat = [[int(i)for i in input().split()]for _ in range(n)]
#print(mat)
s = ''
for i in range(n):
    for j in range(n):
        if i != j:
            if mat[i][j] != mat[j][i]:
                s ="NO"
                break
            else:
                 s ="YES"
            #break
print(s) 
