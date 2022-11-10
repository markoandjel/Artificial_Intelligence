from functools import reduce
def zamena(a:list[int],x:int)->list:
    return list(a[i] if(a[i]>=x) else reduce(lambda l,k:l+k,a[i+1:],0) for i in range(len(a)))

print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))