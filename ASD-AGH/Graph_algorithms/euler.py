def euler(G):
    cycle = []

    def DFS_visit(G, v):
        for _ in range(len(G[v])):
            if len(G[v]) == 0:
                break
            u = G[v].pop(0)
            G[u].remove(v)
            DFS_visit(G, u)
        cycle.append(v)

    DFS_visit(G, 0)
    return cycle


G = [[1, 2], [0, 2, 3, 4], [0, 1, 3, 4], [1, 2], [1, 2]]

print(euler(G))
