# На вход программе подается строка текста. Напишите программу, которая определяет количество различных символов в строке.
myset = set(input())
count = 0
for el in myset:
    if el in myset:
        count += 1
print(count)
