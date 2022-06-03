# Используя генератор множеств, дополните приведенный код, так чтобы получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence. 
# Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

import re
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
sentence1 = re.sub(r'[.,;:-?-!()]', '', sentence)
#sentence1 = sentence.strip('.,();:')
#print(sentence1)
myset = sentence1.split()
myset1 = {s.lower() for s in myset}
print(*sorted(myset1))
