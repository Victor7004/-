# Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для одного данного слова определяет его синоним.
d = {}
n = int(input())
for i in range(n):
    d.setdefault(*input().split(' '))    
a = input()
for keys,values in d.items():
    if keys == a:
        print(values)
    if values == a:
        print(keys)

# Верное решение #431831889
# Python 3

words = {}
for _ in range(int(input())):
    a, b = input().split()
    words[a], words[b] = b, a
print(words[input()])
