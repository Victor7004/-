# На вход подается число N. Найдите его факториал, то есть произведение натуральных чисел от 1 до N:

# N! = 1 \cdot 2 \cdot ... \cdot NN!=1⋅2⋅...⋅N
N = int(input())
sum = 1
for i in range(1,N+1):
    sum *= i
print(sum) 
