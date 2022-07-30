# На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. 
# Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
import re
words1 = re.sub(r'[.,;:-?-!]', '', input().lower().replace(' ', ''))
words2 = re.sub(r'[.,;:-?-!]', '', input().lower().replace(' ', ''))
#w3 = []
#w4 = []
words1 = sorted(words1)
words2 = sorted(words2)
if words1 == words2 :
    print('YES')
else:
    print('NO')
