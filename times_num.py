""" Программа для определения, является ли число произведением 
    двух чисел из данного набора чисел """
n = int(input())                                # Задаем колличество значений для ввода;
number_list = []                                # Создаем пустой список чтобы использовать в цикле;
for i in range(n):                              # Заполняем список из n - значений;
    number_list.append(int(input()))            # считывая вводимые значения:
produkt_number = int(input())                   # Задаем значение произведения;
flag = "НЕТ"                                    # Задаем значение переменной flag;
for i in range(len(number_list)):               # Задаем цикл перебора рашего списка;
    for j in range(len(number_list)):           # Задаем вложеный цикл перебора наш. списка;
        if i == j:                              # Проверяем условие, заданое в условии задачи;
            continue                            # Пропускаем дальнешее выполнение цикла;
        if produkt_number == number_list[i]\    #Задаем условия
                * number_list[j]:               # Проверяем условие;
            flag = "ДА"                         # Если условие верно изменяем flag на "ДА";
            break                               # Прерываем цикл на флаг;
print(flag)                                     # Вывод результата.
