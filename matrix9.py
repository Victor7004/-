# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем nn строк по mm целых чисел в каждой, отделенных символом пробела.

# Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.

# Мое решение:

n, m = int(input()), int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))# считали матрицу n*m 

#for row in l:            # делаем перебор всех строк матрицы A
    #for elem in row:     # перебираем все элементы в строке row
        #print(elem, end = ' ')
    #print()
# находит индексы (строку и столбец) первого вхождения максимального элемента
s = max(max(l, key = max))
for i in range(n):
    if s in l[i]:
        print(i, l[i].index(s))
        break   
# Эталонное решение:
n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
row, col = 0, 0
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[row][col]:
            row,col = i, j
            
print(row, col)
