#Эталонное решение
res = []

for el in input().split():
    if res and el in res[-1]:
        res[-1].append(el)
    else:
        res.append([el])

print(res)

#Мое РЕШЕНИЕ
char_list = []
a = []
for c in input().split():
    if len(a) < 1:
        a.append(c)
    elif len(a) >= 1:
        if a[-1] == c:
            a.append(c)
        elif a[-1] != c:
            char_list.append(a)
            a = []
            a.append(c)
if len(a) > 0:
    char_list.append(a)
print(char_list)
