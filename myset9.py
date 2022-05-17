# На вход программе подаются две строки текста, содержащие числа. 
# Напишите программу, которая определяет количество чисел, которые есть как в первой строке, так и во второй.

# Верное решение #459365138
# Python 3
print(len(set(input().split()) & set(input().split()))) 

# Мое решение
str1 = input().split()
str2 = input().split()
myset1 = set(str1)
myset2 = set(str2)
myset3 = myset1 & myset2
print(len(myset3))
