# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке. 
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
# Мое решение :

ls = [list(input()) for _ in range(int(input()))]
print(*sorted(set(ls.pop()).intersection(*ls)))

# Верное решение #440185382
# Python 3

n = int(input())
numbers = [input() for _ in range(n)]

num_set = set(numbers[0]).intersection(*numbers)
print(*sorted(num_set))
