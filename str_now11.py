# Вводятся три целых положительных числа (максимум трехзначные) через пробел в одну строчку. 
# Для двухзначных и однозначных чисел нужно добавить слева незначащие нули так, чтобы все числа содержали по три цифры. Вывести на экран полученные числа в столбик.
a, b, c = map(str, input().split())
a1 = a.rjust(3, '0')
b1 = b.rjust(3, '0')
c1 = c.rjust(3, '0')
print(a1,b1,c1, sep='\n')
