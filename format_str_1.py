# Вводятся: имя, фамилия и возраст (целое положительное число) каждое значение с новой строки. 
# Используя метод строки format, через индексы переменных необходимо сформировать строку по шаблону:

# "Уважаемый <имя> <фамилия>! Поздравляем Вас с <возраст>-летием!"

Результат вывести на экран (без кавычек)
name = input()
surname = input()
age = int(input())
print('Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!'.format(name, surname, str(age)))
