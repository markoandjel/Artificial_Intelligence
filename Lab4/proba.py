import numpy as np
import queue
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

def subAtPos(mat1,mat2,xypos):
    x,y=xypos
    #mat1 je osnovna matrica
    ysize,xsize=len(mat2),len(mat2[0])
    xmax,ymax=(x+xsize),(y+ysize)
    if xmax>len(mat1) or ymax>len(mat1[0]):
        return False
    else:
        mat1[y:ymax,x:xmax]-=mat2
        return mat1

def solutionCheck(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if not table[i][j] == 1:
                return False
    return True

def generateGraph(table,allFigures):
    graph={'S':[]}
    for fig in allFigures:
        for rot in range(4):
            for i in range(5):
                for j in range(5):
                    if not isinstance(addAtPos(table,allFigures[fig][rot],(i,j)),bool):
                        graph['S'].append(f'{fig} {rot} {i} {j}')
                        graph[f'{fig} {rot} {i} {j}']=[]
                        for fig2 in allFigures:
                            if fig2==fig: continue
                            for rot2 in range(4):
                                for i2 in range(5):
                                    for j2 in range(5):
                                        if not isinstance(addAtPos(table,allFigures[fig2][rot2],(i2,j2)),bool):
                                            graph[f'{fig} {rot} {i} {j}'].append(f'{fig2} {rot2} {i2} {j2}')
    #print(graph)
    return graph



def findSolutionBruteForce(graph,S,allFigures):
    path=list()
    stack_nodes=queue.LifoQueue(len(graph))
    visited=set()
    prev_nodes=dict()
    prev_nodes[S]=None
    visited.add(S)
    stack_nodes.put(S)
    found_dest=False

    while(not found_dest) and (not stack_nodes.empty()):
        node=stack_nodes.get()
        for dest in reversed(graph[node]):
            if dest not in visited:
                values=dest.split(" ")
                prev_nodes[dest]=node
                prev=prev_nodes[dest]
                tablica=np.zeros((5,5))   
                while prev is not None:
                    addAtPos(tablica,allFigures[values[0]][int(values[1])],(int(values[2]),int(values[3])))
                    prev=prev_nodes[prev]
                if solutionCheck(tablica):
                    found_dest=True
                    end=dest
                    break
                #visited.add(dest)
                stack_nodes.put(dest)


    path=list()
    if found_dest:
        path.append(end)
        prev=prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev=prev_nodes[prev]
        path.reverse()
        return path
    else:
        return "Nema resenja"


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
#print(allFigures['red'])

graph=generateGraph(table,allFigures)

solution=findSolutionBruteForce(graph,'S',allFigures)
print(solution)