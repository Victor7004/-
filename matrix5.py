# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# Мое решение :
n = int(input())
m = []
for _ in range(n):
    t = [int(i) for i in input().split()]
    m.append(t)
#print(m)
#for i in range(n):
    #for j in range(n):
        #print(m[i][j], end=' ')
    #print()
mx = []    
for i in range(n):
    #mx = []
    for j in range(n):
        if i >= j:
            mx.append(m[i][j])
print(max(mx)) 

# Эталонное решение :
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)
    
largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest) 
