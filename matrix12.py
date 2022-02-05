# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали, 
# при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали
n = int(input())
mat  = [[int(i) for i in input().split()] for _ in range(n)]
#print(mat)
for i in range(len(mat)):
    h = mat[i][i]
    mat[i][i]=mat[n-1-i][i]
    mat[n-1-i][i]=h
    #for j in range(n):
        #if j == i:
            #mat[i][i], mat[n-i-1][i] = mat[n-i-1][i],mat[i][i]  
            #mat[i][i], mat[i][n-i-1] = mat[i][n-i-1],mat[i][i]
#print(*mat, end='')
for el in mat:
    print(*el)
