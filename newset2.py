# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

print('NO' if set(input()).isdisjoint(set(input())) else 'YES')

# Альтернативный вариант
a = set(input())
b = set(input())
c = a.intersection(b)
if len(c) > 0:
    print('YES')
else:
    print('NO')
