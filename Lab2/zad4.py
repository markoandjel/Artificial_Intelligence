from functools import reduce
def suma(a:list)->int:
    return reduce(lambda x,y : (suma(x) if type(x) == list else x) + (suma(y) if type(y) == list else y), a)

print(suma([[1, 2, 3],[[2,[1,1]], 5, 6],[7, 8, 9]]))