n = int(input())

mat = []                                            # создаем матрицу
for _ in range(n):
  mat.append([int(i) for i in input().split()])

magic = True                                        # устанавливаем флаг

unique = []                                         # пустой список уникальных значений матрицы
for r in range(n):                                  # проверяем все элементы матрицы на уникальность и 0
  for c in range(n):
    if mat[r][c] in unique or mat[r][c] == 0:
      magic = False
      break
    else:
      unique.append(mat[r][c])

total = sum(mat[0])                                 # считаем сумму первой строки матрицы
d1 = 0
d2 = 0
for r in range(n):                                  # проверяем сумму значений главной и побочной диагонали 
  for c in range(n):
    if r == c:
      d1 += mat[r][c]
    if r == n - 1 -c:
      d2 += mat[r][c]  
if not d1 == d2 == total:                            
  magic = False

for i in mat:                                        # проверяем суммы всех строк матрицы
  if sum(i) != total:
    magic = False
    break

tran = [[0]*n for _ in range(n)]                     # создаем транспонированную матрицу
for r in range(n):
  for c in range(n):
    tran[r][c] = mat[c][r]

for j in tran:                                       # проверяем суммы строк(они же столбцы исходной матрицы)
  if sum(j) != total:
    magic = False
    break

if magic == True:
  print('YES')
else:
  print('NO')
