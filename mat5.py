# На вход программе подаются два натуральных числа nn и mm. 
# Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "диагоналями" в соответствии с образцом.

n, m = [int(i)for i in input().split()]
mat = [[0]*m for _ in range(n)]
nm = 0
for q in range(n*m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                mat[i][j] = nm
for el in mat:
    print(*el)
    
# Верное решение #431633581
n, m = map(int, input().split())
mt = [[''] * m for i in '1'* n]
d = 1
for k in range(1, n + m + 1):
    for i in range(n):
        for j in range(m):
            if i + j + 1 == k:
                mt[i][j] = str(d).ljust(3)
                d += 1
[print(*r, sep='') for r in mt]
