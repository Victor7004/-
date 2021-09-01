#Дана строка чисел поменяйте пары рядом стоящих местами
numbers = input().split()

for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    
print(*numbers)
