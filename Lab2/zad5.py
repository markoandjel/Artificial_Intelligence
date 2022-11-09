from itertools import starmap
from functools import reduce
import operator
def proizvod(a:list[list[int]],b:list[int])->list[int]:
    return list(starmap(lambda x, y: reduce(operator.add, x) * y, list(zip(a, b))))

print(proizvod([[1,2,3],[4,5,6],[7,8,9]], [1,2,3]))