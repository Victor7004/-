# На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех трех слов был использован один и тот же набор букв?
str = input().split()
b = set(str[0])
c = set(str[1])
d = set(str[2])
if b == c == d:
    print('YES')
else:
    print('NO')
