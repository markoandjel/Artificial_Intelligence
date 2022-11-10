def broj(rgb:str):
    return int(rgb[1:3],16)*65536+int(rgb[3:5],16)*256+int(rgb[5:7],16)
print( broj("#FA0EA0"))