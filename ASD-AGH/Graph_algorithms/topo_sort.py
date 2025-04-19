def DFS(G):
    visited=[False for _ in range(len(G))]
    parent=[None for _ in range(len(G))]
    sorted_array=[]
    def dfs_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G,v)
        sorted_array.append(u)

    for i in range(len(G)):
        if not visited[i]:
            dfs_visit(G, i)
    sorted_array=sorted_array[::-1]
    return visited,parent,sorted_array


G=[[1,2,5],[2,4],[],[],[3,6],[4],[]]
print(DFS(G))


