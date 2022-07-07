#
lst = [word for word in input().lower().split()]
#print(lst)
result = {}
for sim in lst:
    result[sim] = result.get(sim, -1) + 1
    if result[sim] >= 1:
        print(sim + '_'+str(result[sim]), end = ' ') 
    else:
        print(sim, end = ' ')
