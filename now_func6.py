#  Гелевая ручка стоит x рублей. Сегодня магазин предоставляет скидку в 10% на каждую купленную ручку. 
# Какое наибольшее количество таких ручек можно будет купить на 500 рублей? Результат выведите в консоль в виде целого числа.
# ввод данных
x = int(input())

# здесь продолжите программу
sel = x*0.9
pen = 500 // sel
print(round(pen))