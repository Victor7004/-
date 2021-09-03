#Школьное читабельное решение;
s = [int(n) for n in input().split()]
#создаем переменную счетчик первоначально равную нулю
counter = 0
previous = s[0]
for i in range(len(s)):
  if s[i] > previous:
    counter += 1
  previous = s[i]
print(counter)
