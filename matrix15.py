# На шахматной доске 8 \times 88×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. 
# Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.

start = input()
matrix = [['.' for _ in range(8)] for _ in range(8)]  # b6
pos_x, pos_y = 8-int(start[1]), ord(start[0])-97
matrix[pos_x][pos_y] = 'N'
#print(*matrix, sep='\n')
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (pos_x-i)**2 + (pos_y-j)**2 == 5:
            matrix[i][j]='*'
for el in matrix:
    print(*el)
    
# Верное решение #469418100
x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(y - i) * abs(x - j) == 2:
            board[i][j] = '*'
        
for row in board:
    print(*row)    
