# В летний лагерь нужно отвести n детей и m вожатых с помощью автобусов. Максимальная вместимость каждого автобуса 20 человек. 
# Допишите программу для вычисления минимального числа автобусов, необходимых для перевозки детей вместе с вожатыми. Результат выведите в консоль в виде целого числа.
# ввод данных

n, m = map(int, input().split())

# здесь продолжите программу
if (n+m)%20 == 0:
    bus = (n+m)//20
    print(bus)
else:
    bus = (n+m)//20
    bus += 1
    print(bus)