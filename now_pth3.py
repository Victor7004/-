# Во входной строке записана последовательность чисел через пробел. 
# Для каждого числа выведите слово yes, если это число уже встречалось в последовательности или no, если не встречалось.
numbers = map(int, input().split())
used = set()
for i in numbers:
    n = int(i)
    if n in used:
        print('yes', end=' ')
    else:
        print('no', end=' ')
    used.add(n)
