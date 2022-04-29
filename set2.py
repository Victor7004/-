# В классе учатся 3030 учеников. Среди них 1717 отличников по математике, 1010 отличников по физике и 1313 — по информатике. 
# Трое — отличники по всем предметам, пятеро — по математике и физике, четверо — по физике и информатике, а 66 человек — по математике и информатике. 
# Сколько учеников не являются отличниками ни по одному из этих предметов?


people = 30

categories = [
    ['fi',  4],
    ['mi',  6],
    ['m',  17],
    ['f',  10],
    ['mfi', 3],
    ['mf',  5],
    ['i',  13]
]

def otlichniki(cat_):
    
    def sorter(element):
        return len(element[0])
    
    cat_.sort(key=sorter, reverse=True)
    otl = cat_[0][1]
    
    for item in cat_[1:]:
        idx = cat_.index(item)
        for upper_item in cat_[:cat_.index(item)]:
            if set(item[0]).issubset(set(upper_item[0])):
                item[1] -= upper_item[1]
        otl += item[1]
        
    return otl
    

print(people - otlichniki(categories))
