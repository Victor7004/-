# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
n = int(input())
for i in range(n):
    myset = set()
    s = ''
    s = input().lower()
    for j in s:
        myset.add(j)
    print(len(myset))
