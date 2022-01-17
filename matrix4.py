# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.
# Эталонное решение
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
    
for i in range(n):
    counter = 0
    average = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > average:
            counter += 1
    print(counter)
    
    # Мое решение
    n = int(input())
#matrix = [list(map(int, input().split())) for i in range(int(input()))]1-й способ заполнения матрицы
m = []#2-й способ заполнения матрицы
for i in range(n):
    l = [int(num) for num in input().split()]
    m.append(l)
    #print(*m[i])
for i in m:
    s = 0
    for j in i:
        if j > (sum(i)//len(i)):
            s += 1
    print(s)  
