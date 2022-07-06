# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

lst = [word.strip('.,!?:;-') for word in input().lower().split()]
#print(lst)
result = {}
for sim in lst:
    result[sim] = result.get(sim, 0) + 1 
#print(result)
for key, values in sorted(result.items()):
    if values == min(result.values()):
        print(key)
        break
        
# Верное решение #443948930
# Python 3
# put your python code here
dct = {}
lst = [word.strip('.,!?:;-') for word in input().lower().split()]
for word in lst:
    dct[word] = dct.get(word, 0) + 1
lst = [(value, key) for key, value in dct.items()]
lst.sort()
print(lst[0][1])
