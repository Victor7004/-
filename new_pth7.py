# Напишите программу для расшифровки секретного слова методом частотного анализа.
s = input()
n = int(input())
s2 = []
#for i in range(n)
c = {}
c1 = {}
for i in range(n):
    value, key = input().split(": ")
    c.setdefault(value, int(key))    #value, key = input().split(": "), при добавлении в словарь ключ привести к целому int(key)
    #s1 = input().split()
    #s2.append(s1)
c1 = {v: k for k,v in c.items()}
#print(c1)    
#print(s, n, c )
for j in range(len(s)):
    key = s.count(s[j])
    print(c1[key], end = '')
#1.создаём словарь с цифрами в качестве ключей и буквами в качестве значений

#2.пускаем цикл с range(длина вводимой строки)

#3.в цикле получаем значения нашего словаря по ключу ваша_строка.count(ваша_строка[i]) и выводим их с параметром end="" 
#Удачи! =)

# Верное решение #444071147
# Python 3
dct, word = {}, {}
s = input()
for c in s:
    word[c] = word.get(c, 0) + 1
for _ in range(int(input())):
    a, b = input().split(': ')
    dct[int(b)] = a
for c in s:
    print(dct[word[c]], end='')
