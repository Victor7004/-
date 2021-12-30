# Эталонное решение:
def pascal(n):
    list1 = []
    for i in range(n + 1):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(list1[i-1][j] + list1[i-1][j-1])
        list1.append(temp_list)
    return list1[n]

row = int(input())
print(pascal(row))

# Мое решение:
n = int(input())
p = []
for i in range(n+1):
    row = [1]*(i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row [j] = p[i - 1][j - 1] + p[i - 1][j]
    p.append(row)
#for r in p:
    #print(r)
print(p[n])
