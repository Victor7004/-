# На вход подается трехзначное число. Напечатайте сумму его цифр. 
# Например, если на вход поступило число 125, то результат должен быть 1 + 2 + 5 = 8
number = int(input())
s = str(number)
c = 0
for el in s:
    c += int(el)
print(c)

# Верное решение #367983007
Python 3
text1 = int (input ())
a = text1 //100
b = text1 // 10 % 10
c = text1 % 10
print (a+b+c)
