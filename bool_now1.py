# Вводится стоимость книги X рублей (например, X = 435.78) - положительное вещественное число с точностью до сотых (два знака после запятой). Требуется определить, является ли дробное значение (число после запятой) больше 50. 
# На экран вывести True, если больше и False - в противном случае. Задача делается без использования условного оператора
a=float(input())
b=int(a)
c = (a - b) * 100
print(c > 50)
