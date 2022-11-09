from itertools import zip_longest

def poredak(a:list[int],b:list[int])->list[tuple[int,int,str]]:
    return list(map(lambda x:(x[0],x[1],('Jeste') if x[0]<<1==x[1] else ('Nije')),list(zip_longest(a,b,fillvalue=0))))

print(poredak([1,2,3,4,5,6],[2,4,6,7,8,10,12])) 