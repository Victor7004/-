#Вывод матрицы в обратном порядке
n = 3
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for i in range(n):
    for j in range(n):
        print(a[n - i - 1][n - j - 1], end=' ')
    print()
    
#Выводит:

9 8 7
6 5 4
3 2 1
