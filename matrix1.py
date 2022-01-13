# Мое решение:
n, m = int(input()), int(input())
l = []
for i in range(n*m):#Создаем цикл, диапазон равен n*m. range(n*m)
    l.append(input())#С каждой итерацией просим ввести пользователя строку. Эту строку сразу же добавляем в  список. l.append(input())
    if len(l) == m:#Если длина этого списка равна m, тогда выводим print(*l), обязательно со звёздочкой — она убирает лишние символ. И очищаем данный список.
        print(*l)
        l = []

# Эталонное решение:
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
