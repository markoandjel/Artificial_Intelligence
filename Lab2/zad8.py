from functools import reduce
import operator
def izracunaj(a:list)->list:
    return list(map(lambda x: x if(type(x)==int) else reduce(operator.mul,x),a))

print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))