a = int(input())
c = []
b1, b2, b3, b4 = 0, 0, 0, 0
for i in range(a):
    #x, y = 0, 0
    #x = int(input())
    #y = int(input())
    x, y = map(int, input().split())
    if x > 0 and y != 0:
        if y > 0 and x != 0: # x>0, y>0
            b1 +=1
            #print("Первая четверть:", + b1)
        else: # x>0, y<0
            b2 +=1
            #print("Четвертая четверть:", + b2)
    else:
        if y > 0 and x != 0: # x<0, y>0
            b3 +=1
            #print("Вторая четверть:", + b3)
        #else: # x<0, y<0
        elif y < 0 and x < 0 and y != 0 and x != 0:
            b4 +=1
            #print("Третья четверть:", + b4)
print("Первая четверть:", + b1)
print("Вторая четверть:", + b3)
print("Третья четверть:", + b4)
print("Четвертая четверть:", + b2)
