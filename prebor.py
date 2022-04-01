# Принимаем параметры матрицы
n, m = map(int, input().split())
# Создаем скелет матрицы
matrix = [[0] * m for i in range(n)]
# Задаем отсчет с единицы
d = 1

for k in range(1, n + m):               # Цикл перебирающий сумму индексов в диагонали
    for i in range(n):                  # Перебираем строки
        for j in range(m):              # Перебираем столбцы
            if i + j + 1 == k:          # Выявляем ячейки, относящиеся к искомой диагонали
                matrix[i][j] = d        # Присваиваем обнаруженной ячейке порядковый номер
                d += 1                  # Обновляем счетчик

# Распечатываем полученную матрицу
for row in range(n):
    for col in range(m):
        print(str(matrix[row][col]).ljust(3), end=' ')
    print()
