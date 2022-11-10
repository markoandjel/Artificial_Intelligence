from functools import *
from itertools import *
def spoji(lista):
        A , B= tee(lista)
        C, D = tee(lista)
        next(B, None)
        next(C, None)        
        next(C, None)
        return zip(A, B, C) 
def izracunaj(a:list,func):
    return list(starmap(func, spoji(a)))
print(izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z))
print(list(spoji([2, 5, 1, 6, 7])))