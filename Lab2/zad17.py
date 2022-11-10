
def tekst(txt:str):
    return ''.join(map(lambda x:x if (ord(x) in range(65,91)) or (ord(x) in range(97,123)) or ord(x) in range(48,58) else '\\u'+str((hex(ord(x))[2:]).zfill(4)),txt))

print(tekst("Otpornost 10Ω."))