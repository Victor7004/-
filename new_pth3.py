# В математике функция знак числа sign(x) определена так:

#sign(x) = 1,   если x > 0,
#sign(x) = -1, если x < 0,
#sign(x) = 0,   если x = 0.

# На вход подается число. Напишите программу, которая реализует логику работы функции sign().
x = input()
if float(x) > 0:
    print("1")
elif float(x) < 0:
    print("-1")
else:
    print("0")
# Верное решение #623730020
# Python 3
x = float(input())
print(1 if x > 0 else 0 if x == 0 else -1)
