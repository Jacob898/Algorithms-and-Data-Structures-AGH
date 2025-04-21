#Jakub Stachecki
#Program to zmodyfikowany algorytm Dijkstry do znajdowania najkrótszej ścieżki w grafie,
# który kiedy natrafi na wierzchołek, który jest osobliwością, oprócz swoich sąsiadów przegląda także
#wierzchołki które są osobliwością z długością krawędzi(w programie edge) równą 0. Złożoność czasowa to O(V^2)
from zad5testy import runtests
from queue import PriorityQueue


def relax(Q, d, v, edge, u):
    if d[v] > d[u] + edge:
        d[v] = d[u] + edge
        Q.put((d[v], v))


def Dijkstra(n, G, S, start, finish):
    d = [float('inf') for _ in range(n)]
    d[start] = 0

    Q = PriorityQueue()
    Q.put((0, start))

    while not Q.empty():
        distance, u = Q.get()
        for v, edge in G[u]:
            relax(Q, d, v, edge, u)
        if u in S:
            for v in S:
                relax(Q, d, v, 0, u)

    if d[finish] != float('inf'):
        return d[finish]
    return None


def spacetravel(n, E, S, a, b):

    G = [[] for _ in range(n + 1)]
    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    return Dijkstra(n, G, S, a, b)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
