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
# Верное решение #448815421
# Python 3
def s(word):
    res = {}
    for i in word.lower():
        if i.isalpha():
            res[i] = res.get(i, 0) + 1
    return res


print(("NO", "YES")[s(input()) == s(input())])
