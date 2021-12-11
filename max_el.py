list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

for li in list1:
    if max(li) > maximum:
        maximum = max(li)
print(maximum)

# выведет
106
