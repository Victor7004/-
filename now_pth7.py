# На вход программы подается число. Напишите функцию, которая возвращает произведение цифр, из которых это число состоит.
# Например, число 3279 состоит из цифр 3, 2, 7, 9, их произведение 3*2*7*9 = 378.

number = input()        
#s = 1
def product(number):
    s = 1
    if len(number) == 0:
        return 1
    else:
        for num in number:
            #print(num)
            pro_num = 1   
            s *= pro_num *int(num)
            #print(s)
    return s

result = product(number)
print(result)
