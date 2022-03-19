# Напишите программу, которая возводит квадратную матрицу в mm-ую степень.
import copy
n = int(input())
A = []
for i in range(n):
    temp=[int(i) for i in input().split()]
    A.append(temp)
m = int(input())
stp = m
A1 = copy.deepcopy(A)
for stp in range(stp - 1):
    A2 = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):   
        for j in range(n):
            for k in range(n):
                A2[i][j] += A1[i][k] * A[k][j]
    A1 = copy.deepcopy(A2)
for el in A2:
    print(*el)
    
# Верное решение #469420164
def square_matrix_mult(matrixA, matrixB, size):
    matrixC = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for q in range(size):
                matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
    return matrixC
    
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
powered_matrix = matrix.copy()

for _ in range(m - 1):
    powered_matrix = square_matrix_mult(matrix, powered_matrix, n)

for row in powered_matrix:
    print(*row)
