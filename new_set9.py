# Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала учебного года. 
# Для каждого урока есть листок со списком присутствовавших учеников.

# Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.
m = int(input())
n = int(input())
first_set = set([input() for _ in range(n)])
empty_set = set()
if n == 1:
    print(*first_set)
else:
    for i in range(m-1):
        for j in range(int(input())):
            empty_set.add(input())
        first_set.intersection_update(empty_set) 
        empty_set.clear() 
    first_set = sorted(first_set)
    for row in first_set:
        print(row)
