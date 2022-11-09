from functools import reduce
def objedini(A:list):
   return dict(reduce(lambda acc,el: acc | {str(el[0]): el[1:] if el[1:] else None}, A, dict()))

print(objedini([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)]))