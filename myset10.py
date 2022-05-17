# На вход программе подаются две строки текста, содержащие числа. 
# Напишите программу, которая выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй.
# Верное решение #469403081
# Python 3
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())

print(*sorted(set1 & set2))

# Мое решение
myset = set(sorted(input().split())) & set(sorted(input().split()))
mylist1 = []
for el in myset:
    mylist1.append(int(el))
print(*(sorted(mylist1)))
