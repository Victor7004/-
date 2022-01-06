# На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

# Верное решение #468145093
def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))

# Мое решение
def chunked(s, n):
    res = []
    temp = []
    for el in s:
        temp.append(el)
        #print(temp)
        if len(temp) == n:
            res.append(temp)
            temp = []
    if len(s) % n != 0:
        res.append(temp)
        
    #print(temp)
    print(res)    
s = input().split()
n = int(input())
chunked(s, n)  

# Sample Input 4:

# a b c d e f r g b
# 2
# Sample Output 4:

# [['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
