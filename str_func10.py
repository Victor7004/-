# С клавиатуры вводятся две буквы (в одну строку через пробел). Вывести на экран следующую строку:
#"Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"

a, b = map(str, input().split())
print("Коды:", a +" =",str(ord(a))+",", b,"=", str(ord(b))
