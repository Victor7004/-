# На летних каникулах Тимур и ученики онлайн-школы BEEGEEK решили отдохнуть. 
# В результате nn учеников школы поехали отдыхать на море, mm учеников съездили в деревню, а kk учеников сходили в горы. 
# Оказалось, что и в деревне, и на море были xx учеников, а в деревне и в горах — yy учеников. Побывать и в горах, и на море не удалось никому. 
# Напишите программу для определения количества учеников в школе, если никто не смог посетить все три места сразу,
# а zz учеников писали ДВИ по математике для поступления в МГУ, и никуда не ездили.

# Верное решение #469328362

#Python 3

n, m, k, x, y, z = [int(input()) for _ in range(6)]

print(n + m + k - x - y + z)
