from queue import Queue


#zadanie 1a
def bipartite(G, start_v):
    colors = [-1] * len(G)
    q = Queue()
    q.put(start_v)
    colors[start_v] = 0
    while not q.empty():
        v = q.get()
        for u in G[v]:
            if colors[u] == -1:
                colors[u] = (colors[v] + 1) % 2
                q.put(u)
            else:
                if colors[u] == colors[v]:
                    return False
    return True


#testy
G = [[3, 4], [3, 5], [3, 5], [0, 1, 2], [0], [1, 2]]
print(bipartite(G, 0))
