language = [('C',1972),('C++',1985),('Java',1995),('JavaScript',1995),('PHP',1994),('Pyrhon',1991),]

print(list(filter(lambda item:item[1] < 1990 ,language)))
