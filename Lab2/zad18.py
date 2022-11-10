import re
def brojevi(txt:str):
    return list(map(lambda x:int(x),re.findall(r"\d+",txt)))
print(brojevi('42+10=52;10*10=100'))