# Напишите программу, которая поворачивает квадратную матрицу чисел на 90^{\circ}90 
∘
  по часовой стрелке.
n = int(input())
mat = [[int(i) for i in input().split()] for _ in range(n)]
mat.reverse()
for i in range(n):
    for j in range(n):
        print(mat[j][i], end = ' ')
    print()
    
# Верное решение #469418010
n = int(input())
matrix = [input().split() for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[i][j] = matrix[n - j - 1][i]

for row in result:
    print(*row)

