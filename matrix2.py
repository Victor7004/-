# Мое решение:
n = int(input())
m = int(input())
l=[[0]*m for _ in range(n)]#Заполняю матрицу нулями с помощью генератора списков.  
#print(l)
for i in range(n):#для i в ряду n:  
    for j in range(m):#для ж в ряду м:
        l[i][j] = input()#матрица[i][j] = ввод()
    print(*l[i])#вывожу каждую строку матрицы (*матрица[i])    
print()#отступ строки
k = 0
for j in range(m):#для j в ряду м:
    for i in range(n):#для i в ряду n:
        print(l[i][j], end=' ')#вывожу каждый элемент, на конце пробел, т.е.: (матрица[i][j], конец = ' ')
    print()
    
# Эталонное решение: 
n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = [input() for j in range(m)]
    matrix.append(row)
    
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()
