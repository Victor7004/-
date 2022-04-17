# Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические значения чисел каждого вложенного кортежа в заданном кортеже кортежей numbers.

a = []
count = 0
for i in range(len(numbers)):
    tot = 0
    count = 0
    for j in range(len(numbers[i])):
        tot += numbers[i][j]
        count += 1
    a.append(tot/count)
print(a)
