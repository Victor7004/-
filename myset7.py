# Напишите программу для определения общего количества различных слов в строке текста.
lst = input().lower().split()
for i in range(len(lst)):
    lst[i] = lst[i].strip(".,;:-?!")
myset = set()
for j in lst:
        myset.add(j)
print(len(myset))
