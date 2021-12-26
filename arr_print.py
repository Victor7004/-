# Эталонное решение
n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')


# Мое решение
n = int(input()) 
count = 1
my_list1 = []
my_list2 = []
m = 0
for z in range(n):
    
    for i in range(1, n+1):
        my_list1.append(i)
    #for z in range(n):
        #my_list2.append(z)
        
    print(my_list1)
    my_list1 = []
