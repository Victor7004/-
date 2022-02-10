# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
# Мое решение
n = int(input())
mat = [[int(i) for i in input().split()]for _ in range(n)]
#print(mat)
mat1 = mat[::-1] 
#print(mat[::-1])
for el in mat1:
    print(*el)
    
# Верное решение #433332609
n = int(input())

matrix = [[int(item) for item in input().split()] for _ in range(n)]
matrix.reverse()

for row in matrix:
    print(*row)
