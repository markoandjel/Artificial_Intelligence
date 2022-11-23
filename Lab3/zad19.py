import queue 

def Obilazak(graph,S,M):
    if S is M:
        path=list()
        path.append(S)
        return path
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
                prev_nodes[dest]=node
                if dest is M:
                    found_dest=True
                    break
                visited.add(dest)
                stack_nodes.put(dest)

    path=list()
    if found_dest:
        path.append(M)
        prev=prev_nodes[M]
        while prev is not None:
            path.append(prev)
            prev=prev_nodes[prev]
        path.reverse()

    return path


def ciklicniObilazak(graph,S,M):
    pom=Obilazak(graph,S,M)
    temp=Obilazak(graph,M,S)
    if(len(pom)==0 or len(temp)==0):
        return 'Nema ciklicnog zatvaranja'
    else:
        return pom[:-1]+temp


graph={
    'A':['C','D'],
    'B':['A'],
    'C':['F'],
    'D':['G','H'],
    'E':['B'],
    'F':[],
    'G':[],
    'H':['E']
    }

print(ciklicniObilazak(graph,'D','E'))