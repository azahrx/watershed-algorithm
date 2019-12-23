graf_awal = {'a':{'b':5,'c':4},
            'b':{'c':1,'d':8},
            'c':{'b':2,'e':6},
            'd':{'e':3},
            'e':{'d':5}}

def dijkstra(graph, start, goal):    
    shortpath = {}
    neighbor = {}
    satu = graph
    inf = 999
    path = []
    
    for node in satu:
        shortpath[node] = inf
    shortpath[start] = 0

    while satu:
        resnode = None
        print(shortpath)
        print(neighbor)
        
        for node in satu:
            if resnode is None:
                resnode = node
            elif shortpath[node] < shortpath[resnode]:
                resnode = node

        print(resnode)
        print()
        for current, w in graph[resnode].items():
            if w + shortpath[resnode] < shortpath[current]:
                shortpath[current] = w + shortpath[resnode]
                neighbor[current] = resnode
        satu.pop(resnode)
    
    current = goal

    while current != start:
        try:
            path.insert(0,current)
            current = neighbor[current]
        except:
            print("Path cannot be reached!")
            break

    path.insert(0,start)
    if shortpath[goal] != inf:
        print(shortpath)
        print(path)

print("Shortest path is:")
# Output adalah jarak path terdekat dari a ke e
dijkstra(graf_awal, 'a', 'e')
