mylist = list(input().split('О'))
print(len(max(mylist)))
#Зачем цикл, зачем map?
#map здесь не нужен, как мне кажется, max() прекрасно делает свою работу, если мы говорим о длине последовательности после того, как применили split()
