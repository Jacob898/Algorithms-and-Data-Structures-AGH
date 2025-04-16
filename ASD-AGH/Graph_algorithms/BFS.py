from queue import Queue
#O(V+E)
def BFS(G,s):
    visited=[False for _ in range (len(G))]
    parent=[None for _ in range (len(G))]
    d=[-1 for _ in range(len(G))]
    d[s]=0
    Q=Queue()
    visited[s]=True
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visited[v]:
                d[v]=d[u]+1
                visited[v]=True
                parent[v]=u
                Q.put(v)
    return d,parent

G=[[1],[2],[3,4],[2,4,5],[2,3],[3]]
print(BFS(G,0))