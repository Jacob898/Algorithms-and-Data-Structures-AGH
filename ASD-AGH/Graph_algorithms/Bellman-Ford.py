#O(VE)
def BellmanFord(G, s):
    V = len(G)
    d = [float('inf')] * len(G)
    d[s] = 0
    for _ in range(V - 1):
        for v in range(V):
            for u, edge in G[v]:
                if d[v] > d[u] + edge:
                    d[v] = d[u] + edge
    #sprawdzenie czy nie ma cyklu
    for i in range(V):
        for u, edge in G[i]:
            if d[u] > d[i] + edge:
                return False

    return d

G=[[(2,-1)],[(0,-1)],[(1,1)]]
print(BellmanFord(G,2))
