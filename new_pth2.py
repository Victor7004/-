# На вход подаются два трехзначных числа. Верните True, если суммы цифр в них равны и False -- если не равны.
a, b = map(int, input().split())
a1 = a % 10
a2 = a % 100 // 10
a3 = a // 100
b1 = b % 10
b2 = b % 100 // 10
b3 = b // 100

if (a1+a2+a3==b1+b2+b3):
    print("True")
else:
    print("False")
