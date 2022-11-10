from functools import reduce
def izracunaj(a:list)->list:
    return list(map(lambda x: x**2 if(type(x)==int) else reduce(lambda t,l:t+l,list(map(lambda k:k**2,x))),a))

print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))