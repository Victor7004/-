# Дополните приведенный код, используя генератор, так, чтобы получить словарь result , 
# в котором ключом будет строка – элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.
words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
result = {}
result = {s:[ord(y)for y in s]for s in words}
