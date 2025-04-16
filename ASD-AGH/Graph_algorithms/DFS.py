#O(V+E)

def DFS(G,s):
    visited=[False for _ in range(len(G))]
    parent=[None for _ in range(len(G))]
    def dfs_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G,v)
    dfs_visit(G,s)
    return visited,parent

G=[[1],[2],[3,4],[2,4,5],[2,3],[3]]
print(DFS(G,0))


