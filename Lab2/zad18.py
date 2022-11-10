import re
def brojevi(txt:str):
    return re.findall(r"\d+",txt)
print(brojevi('42+10=52;10*10=100'))