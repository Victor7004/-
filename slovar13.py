#
d = {}
n = int(input())
for i in range(n):
    d.setdefault(*input().split(' '))    
a = input()
for keys,values in d.items():
    if keys == a:
        print(values)
    if values == a:
        print(keys)
