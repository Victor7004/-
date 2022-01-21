# Суммы четвертей
# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
#Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.
# Мое решение:
n = int(input())
m = []
for _ in range(n):
    t = [int(i) for i in input().split()]
    m.append(t)
#print(m)
a, b, c, d = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if i < j and i > n - 1 - j:
            b +=m[i][j]        
        if i > j and i < n - 1 - j:
            d += m[i][j]
        if i < j and i < n - 1 - j:
            a +=m[i][j]        
        if i > j and i > n - 1 - j:
            c += m[i][j]
print('Верхняя четверть:', a)
print('Правая четверть:', b)
print('Нижняя четверть:', c)
print('Левая четверть:', d)

# Эталонное решение: 

n = int(input())
matrix = []
quadrants = [['Верхняя четверть:', 0], 
             ['Правая четверть:', 0],
             ['Нижняя четверть:', 0], 
             ['Левая четверть:', 0]]

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i < j and i + j + 1 < n :
            quadrants[0][1] += matrix[i][j]
        elif i < j and i + j + 1 > n:
            quadrants[1][1] += matrix[i][j]
        elif i > j and i + j + 1 > n:
            quadrants[2][1] += matrix[i][j]
        elif i > j and i + j + 1 < n:
            quadrants[3][1] += matrix[i][j]

for i in range(4):
    print(quadrants[i][0], quadrants[i][1])
