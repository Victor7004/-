# На вход программе подается строка текста, содержащая числа.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
# Верное решение #469560116
# Python 3

numbers = [int(i) for i in input().split()]
myset = set()

for i in numbers:
    if i in myset:
        print('YES')
    else:
        print('NO')
        myset.add(i)
        
        
# Мое решение 
str = input().split()
myset = set()
for j in str:
    if int(j) not in myset:
        myset.add(int(j))
        print('NO')
    else:
        print('YES')
