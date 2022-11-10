from itertools import groupby
def brojanje(text:str):
    return len(list(filter(lambda x:x>1 ,list((len(list(g))) for k,g in groupby(text)))))

print(brojanje('aatesttovi'))