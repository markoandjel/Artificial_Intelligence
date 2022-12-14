import numpy as np

def figures(fig):
    niz=[]
    for i in range(4):
        niz.append(np.rot90(fig,i).tolist())
    return niz

def addAtPos(mat1,mat2,xypos):
    x,y=xypos
    #mat1 je osnovna matrica
    ysize,xsize=len(mat2),len(mat2[0])
    xmax,ymax=(x+xsize),(y+ysize)
    if xmax>len(mat1) or ymax>len(mat1[0]):
        return False
    else:
        mat1[y:ymax,x:xmax]+=mat2
        return mat1
def findSolution(table):
    return True


green=[[1,0,0],[1,0,0],[1,1,1]]
blue=[[1,0,0],[1,1,0],[1,1,0]]
orange=[[1,1,0],[1,0,0],[1,1,0]]
red=[[0,1,0],[1,1,1],[0,0,1]]
yellow=[[1,1,0,0],[0,1,1,1]]

allFigures={'green':figures(green),'blue':figures(blue),'orange':figures(orange),'red':figures(red),'yellow':figures(yellow)}

table=np.zeros((5,5))
pos=(3,3)
mat=addAtPos(table,allFigures['red'][3],pos)
#mat2=addAtPos(mat,allFigures['red'][2],pos)
print(allFigures['red'])