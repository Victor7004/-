# Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.
#  Мое решение :
n = int(input())
m = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    m.append(temp)
    #print(*m[i])
s = 0
for i in range(n):
    s += m[i][i]
print(s) 
# Эталон:
res = 0
for i in range(int(input())):
    res += int(input().split()[i])
print(res)
