# На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её в соответствии с образцом.
n, m = input().split()
matrix = [[i for i in ('.' * int(m))]for i in range(int(n))]
count = 0
for i in range(int(m)):
    for j in range(int(n)):
        count +=1
        matrix[j][i] = count
for el in matrix:
    print(*el)
