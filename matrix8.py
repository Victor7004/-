# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
# Мое решение:
n, m = int(input()), int(input())
for i in range(n):
    mult = []
    for j in range(m):
        mult.append(str(i*j).ljust(3))
    print(*mult)
    
 # Эталон:
n, m = int(input()), int(input())
mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()
