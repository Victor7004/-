#считает количество вхождений разных чисел в списке
mylist = list(input().split())
counter = 1
n = len(mylist)
for i in range(0, n -1):
    if mylist[i] != mylist[i + 1]:
        counter += 1
print(counter)
