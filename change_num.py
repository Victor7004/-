#Дана строка чисел поменяйте пары рядом стоящих местами
numbers = input().split()
#через цикл перебираем все пары значений строки по индексу и меняем их местами
#длина шага 2 от 0 до длины numbers
for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#распаковуем строку в принте    
print(*numbers)
