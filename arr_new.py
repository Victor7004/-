# Эталонное решение:
n = int(input())
result = []

for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))

print(*result, sep='\n')

# Мое решение:
n = int(input())
result = []
#for _ in range(n):
for i in range(1, n + 1):
    result.append(i)

    print(result)
