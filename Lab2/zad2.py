from itertools import zip_longest

def spojidict(a:list[int],b:list[int])->list[dict]:
    return list(map(lambda x:{'prvi':x[0],'drugi':x[1]},list(zip_longest(a,b,fillvalue='-'))))

print(spojidict([1, 7, 2, 4], [2, 5, 2]))