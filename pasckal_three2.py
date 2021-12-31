# Эталонное решение:
#-------------------ФУНКЦИЯ-------------------
def pascal(n):
    triangle = [[1]]
    
    for i in range(n - 1):
        row = [1]
        for j in range(1, len(triangle[i])):
            row += [sum(triangle[i][j - 1: j + 1])]
        row += [1]
        triangle.append(row.copy())
        
    return triangle

#--------------------ВЫЗОВ--------------------
[print(*row) for row in pascal(int(input()))]

# Мое решение:
n = int(input())
p = []
for i in range(n):
    row = [1]*(i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row [j] = p[i - 1][j - 1] + p[i - 1][j]
    p.append(row)
for r in p:
    print(*r)
# Выведет если n=4 :
# 1
# 1 1
# 1 2 1
# 1 3 3 1
