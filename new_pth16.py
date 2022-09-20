# Найдите и выведите в порядке возрастания все двузначные числа, которые равны утроенному произведению своих цифр и выведите результат в виде списка.  
# Числа в списке должны быть расположены в порядке возрастания.
result = []
for i in range(1,100):
    if i == 3*(i%10)*(i//10):
        result.append(i)

print(result)