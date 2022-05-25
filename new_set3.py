# Даны по 1010-балльной шкале оценки по физике трех учеников. 
# Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())
print(*sorted((set1 | set2 | set3)-(set1 | set2), reverse = True))

# 
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted(set3 - set2 - set1, reverse=True))
