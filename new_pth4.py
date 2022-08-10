# На вход программа получает три целых числа. Выведите наибольшее.
s = input().split()
#print(s)
if int(s[0]) > int(s[1]):
    if int(s[1]) > int(s[2]):
        print(s[0])
    else:
        if int(s[2]) > int(s[0]):
            print(s[2])
elif int(s[0]) < int(s[1]):
    if int(s[1]) > int(s[2]):
        print(s[1])
    else:
        print(s[2])
