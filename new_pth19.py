# Бегун готовится к соревнованиям. Сейчас он может пробежать start километров, а на соревнованиях ему нужно будет пробежать goal километров. До соревнования осталось days дней. 
# Во время подготовки к соревнованиям спортсмен может увеличивать дистанцию, которую он пробегает, не больше чем на 10% в день.

start, goal, days = map(int, input().split())
i=0
while i<=days:    
    if  start>=goal:        
        print('True')
        break
    else:
        start*=1.1
        i=i+1          
else:
     print("False")
