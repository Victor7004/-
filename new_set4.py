# Даны по 1010-балльной шкале оценки по биологии трех учеников. Напишите программу, которая выводит множество оценок, не встречающихся ни у одного из трех учеников.

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())
set4 = set()
for i in range(11):
    set4.add(i)
#print(set4)
print(*sorted((set4)-(set1 | set2 | set3)))

# Верное решение #469405777
# Python 3
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set(range(11)) - set1 - set2 - set3))
