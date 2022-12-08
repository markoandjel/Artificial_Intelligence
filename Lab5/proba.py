
def funkcija(G,c):
    stack={
        'uncolored' : list(G.keys()),
        'graph' : { x: list(c) for x in G.keys() },
        'colored': {},
        'prev': None
    }
    return 

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D','C'],
    'C' : ['A', 'E', 'B'],
    'D' : ['B', 'E'],
    'E' : ['C', 'D']
}

colors = set({ 'R', 'G', 'B' })

funkcija(graph,colors)