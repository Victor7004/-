# Дополните приведенный код, чтобы он вывел сумму квадратов элементов множества numbers.
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
numbers = list(numbers)
num = []
for el in numbers:
    num.append(el*el)
print(sum(num))  
