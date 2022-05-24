# Даны по 1010-балльной шкале оценки по математике трех учеников. 
# Напишите программу, которая выводит множество оценок, имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted((set1 | set2 | set3)-(set1 & set2 & set3)))

# Верное решение #432542475
# Python 3
s1, s2, s3 = [set(map(int, input().split())) for _ in range(3)]
print(*sorted((s1 | s2 | s3) - (s1 & s2 & s3)))
