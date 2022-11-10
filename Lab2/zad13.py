from itertools import *
def skupi(a:list[list[int]]):
    return list(starmap(lambda x, y: list(map(lambda c: c[0] + c[1],zip_longest(x, y , fillvalue=0))),pairwise(a)))

print(skupi([[1, 3, 5],[2, 4, 6],[1, 2]]))