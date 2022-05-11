# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
n = int(input())
myset = set()
for i in range(n):
    myset = myset | set(input().lower())        
print(len(myset))
