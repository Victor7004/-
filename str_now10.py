# Вводится строка (слаг). Замените в этой строке все двойные дефисы (--) и тройные (---) на одинарные (-). 
Подумайте, в какой последовательности следует выполнять эти замены. Результат преобразования выведите на экран.
str = input()
print(str.replace('---','--').replace('--','-'))
