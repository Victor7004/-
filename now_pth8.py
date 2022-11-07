# 2520 -- это самое маленькое число, которое можно разделить на каждое из чисел от 1 до 10 без остатка. 
# Какое самое маленькое число, которое можно разделить без остатка на все числа от 1 до 14?

# Напишите функцию, которая выводит это число.
a = 14
def print_number(a):
    for number in range(1,10000000):
        numbers = []
        for delitel in range(1,a + 1):
            if number % delitel == 0:
                numbers.append(delitel)
            if (len(numbers)) == a:
                return(print(number))
print_number(a)
