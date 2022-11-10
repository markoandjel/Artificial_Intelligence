from functools import *
from itertools import *
 
def izracunaj(A:list,func):
    return list(starmap(func,list((A[x],A[x+1],A[x+2]) for x in range(len(A)-2))))

print(izracunaj([2, 5, 1, 6, 7], lambda x, y, z: x + y * z))