
def promeni(a:list[int],x:int)->list[int]:
    return list(map(lambda t: t-x if(t>=x) else t+x,a))

print(promeni([7, 1, 3, 5, 6, 2], 3))