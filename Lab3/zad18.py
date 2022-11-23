import queue

def Farthest(graph,S):
    queue_nodes=queue.Queue(len(graph))
    visited=set()
    prev_nodes=dict()
    prev_nodes[S]=None
    visited.add(S)
    queue_nodes.put(S)
    farthest=list()
    max=0
    while(not queue_nodes.empty()):
        node=queue_nodes.get()
        for dest in graph[node]:
            if dest not in visited:
                prev_nodes[dest]=node
                visited.add(dest)
                queue_nodes.put(dest)

        path=list()
        path.append(node)
        prev=prev_nodes[node]
        while prev is not None:
            path.append(prev)
            prev=prev_nodes[prev]
        if(len(path)>max):
            farthest.clear()
            max=len(path)
            farthest.append(node)
        elif (len(path)==max):
            farthest.append(node)


    return farthest


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

print(Farthest(graph,'D'))


