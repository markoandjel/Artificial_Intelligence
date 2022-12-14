
def func(G,c):
    stack = [{
        'uncolored' : list(G.keys()),
        'domain' : { x: list(c) for x in G.keys() },
        'colored': {},
        'prev': None
    }]
    solution = None
    while stack and not solution:
        top, *stack = stack
        if not top['uncolored']:
            solution = top['colored']
        else:
            to_color = top['uncolored'][0]
            potential = list(top['domain'][to_color])
            for n in G[to_color]:
                if top['colored'].get(n) and top['colored'][n] in potential:
                    potential.remove(top['colored'][n])
            if potential:
                newDomain = dict(top['domain'])
                newDomain[to_color] = potential
                for n in G[to_color]:
                    if potential[0] in newDomain[n]:
                        newDomain[n].remove(potential[0])
                stack.append({
                    'uncolored': sorted([x for x in top['uncolored'] if x is not to_color], key=lambda x: len(newDomain[x])),
                    'domain': newDomain,
                    'colored': top['colored'] | { to_color: potential[0] },
                    'prev': top
                })
            elif top['prev']:
                stack.append(top['prev'])
    return solution

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D','C','E'],
    'C' : ['A', 'E', 'B'],
    'D' : ['B', 'E'],
    'E' : ['C', 'D','B']
}

colors = set({ 'R', 'G', 'B' })
print(func(graph,colors))
    