# На вход программы подается список чисел. Напишите функцию, которая вычисляет произведение чисел этого списка и возвращает ответ.
numbers = map(int, input().split())        

def product(numbers):
    pro_numbers = 1
    for number in numbers:
        pro_numbers *= number
    return pro_numbers
result = product(numbers)
print(result)
