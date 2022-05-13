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
        
