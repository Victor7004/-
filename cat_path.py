# На вход программа получает серию и номер паспорта в формате 4110679874. Добавьте пробел после серии.
#  Подсказка: используйте суши-оператор. 
s= input()
print(s[0:4]+' '+ s[4:])