#O(V^3)
from math import inf

V = [[0, 5, inf, 10],
     [inf, 0, 3, inf],
     [inf, inf, 0, 1],
     [inf, inf, inf, 0]]
n = len(V)
P=[[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if V[i][j]!=inf:
            P[i][j]=i

for k in range(n):
    for x in range(n):
        for y in range(n):
            if(V[x][y]>V[x][k]+V[k][y]):
                V[x][y]=V[x][k]+V[k][y]
                P[x][y]=P[k][y]
print(V,"parent",P)
