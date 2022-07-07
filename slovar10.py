# На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов. 
# Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
lst = [word for word in input().lower().split()]
#print(lst)
result = {}
for sim in lst:
    result[sim] = result.get(sim, -1) + 1
    if result[sim] >= 1:
        print(sim + '_'+str(result[sim]), end = ' ') 
    else:
        print(sim, end = ' ')
# Верное решение #443956403
lst = input().split()
res = {}
for c in lst:
    if c in res:
        print(f'{c}_{res[c]}', end=' ')
    else:
        print(c, end=' ')
    res[c] = res.get(c, 0) + 1
