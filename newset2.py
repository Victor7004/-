# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

print('NO' if set(input()).isdisjoint(set(input())) else 'YES')
