# Дан список чисел. Выведите все различные числа в нем на экран в порядке возрастания
numbers = map(int, input().split())
sorted_numbers = set(numbers)
print(*sorted(sorted_numbers))
