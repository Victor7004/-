#На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список. 
#Верное решение
def get_sublists(symbols, n):
    sublists = []
    for i in range(len(symbols) - n + 1):
        sublists.append(symbols[i:i + n])
    return sublists
    
symbols = input().split()
result = [[]]

for i in range(1, len(symbols) + 1):
    result.extend(get_sublists(symbols, i))

print(result)

#
s = input().split()
e = []
v = [[]]
d = []
#e = s.split
for i in range(len(s)):
     for j in range(len(s)):
        d = s[j:i+j+1]   
        if len(d) == i + 1:
            v.append(d)
print(v)  
