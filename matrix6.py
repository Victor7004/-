# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
# Мое решение
n = int(input())
m = []
for _ in range(n):
    t = [int(i) for i in input().split()]
    m.append(t)         
#print(m)
mx = []
for i in range(n):
    for j in range(n):
        if i >= j and i <= n - 1 - j:
            mx.append(m[i][j])    
        if i <= j and i >= n - 1 - j:
            mx.append(m[i][j])
#print(mx)
print(max(mx))

# Эталонное решение
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
    
largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                
print(largest)
