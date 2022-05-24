# Даны по 1010-балльной шкале оценки по математике трех учеников. 
# Напишите программу, которая выводит множество оценок, имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())

print(*sorted((set1 | set2 | set3)-(set1 & set2 & set3)))
