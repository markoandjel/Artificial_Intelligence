from functools import reduce
def proizvod(a:list[list[int]])->int:
    return reduce(lambda x,y : (proizvod(x) if type(x) == list else x) * (proizvod(y) if type(y) == list else y), a)

print(proizvod(([[1, 3, 5],[2, 4, 6],[1, 2, 3]])))