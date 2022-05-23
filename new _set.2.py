# Даны по 1010-балльной шкале оценки по информатике трех учеников. 
# Напишите программу, которая выводит множество оценок, которые есть и у первого и у второго учеников, но которых нет у третьего ученика

a,b,c = [int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]
a = set(a)
b = set(b)
c = set(c)
#print( *(set(a)&set(b)-set(c)))
d = []
e = set()
e = set(a)&set(b)-set(c)
#print(e)
for el in e:
    d.append(el)
k = []
for i in d:
    k.append(i)
#k.reverse()
#print(*k)
k.sort()
k.reverse()
print(*k)

# Верное решение #469401643
# Python 3

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set1 & set2 - set3, reverse=True))
