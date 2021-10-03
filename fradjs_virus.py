# решение через функцию del
n = int(input())
number_fradjs = []
for i in range(1, n+1):
    code_name = ['a','n','t','o','n']
    fradjs = input()
    for j in fradjs:
        if j in code_name[0]:
            del code_name[0]
        if len(code_name) == 0:
            number_fradjs.append(i)
            break
print(*number_fradjs)
