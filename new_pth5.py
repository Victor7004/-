# На вход программе подается список стран и городов каждой страны. 
# Затем даны названия городов. Напишите программу, которая для каждого города выводит, в какой стране он находится.
c = {}
n = int(input())
s = []
for i in range(n):
    b = input().split()
    c.setdefault(b[0], b[1:])
#print(c)
z = int(input())
for i in range(z):
    y = input()
    s.append(y)
#print(s)    
for h in s:
    for i, j in c.items():    #перебираем пару ключ:значение
        if h in j:
            print(i)
       #Создал пустой словарь  с = {}
#переменная = инт(инпут())
#цикл в длину перменной инпута
#переменная(б) = ввод. сплит
#с.сетдефолт(б[0],б[1:]

#з =  инт(инпут())
#цикл i по длине з
#переменная(у) инпут
#цикл по с :                # с это словарь, который мы заполнили выше, сейчас по его ключам перебираем содержимое
#условие если у в с[i]

#печатаем (i)
Верное решение #431923591
Python 3
d = {}
for _ in range(int(input())):
    country, *cities = input().split()
    for c in cities:
        d[c] = country
for _ in range(int(input())):
    print(d[input()])
