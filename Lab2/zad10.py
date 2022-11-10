from itertools import pairwise
def stepen(a:list[int])->list[int]:
    return list(map(lambda x:x[0]**x[1] ,list(pairwise(a))))

print(stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]))