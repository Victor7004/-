# Вводится целое положительное число n. Выведите True, если число простое и False, если составное (то есть, имеет делители, отличные от 1 и самого себя).
number = int(input())
count = 0
for i in range(2, number - 1):
    if number % i == 0:
        count = count + 1
print("True" if count < 2 else "False" )
