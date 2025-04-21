#Jakub Stachecki
#program działa na zasadzie zmodyfikowanego algorytmu dijkstry. Tworzona jest dodatkowa macierz krawędzi jaką można przejść dwumilowymi butami,
#i uruchamiany jest algorytm Dijkstry. Każdy wierzchołek przyjmuje dwie wartości odległości, jedna bo dotarciu do niego dwumilowymi butami, a druga po dotarciu do niego normalnie.
#Jest to zrobione, by eliminować błędy w przypadku grafu np. takiego jak na przykładzie w treści zadania. W przypadku rozpatrywania wierzchołka z którego możemy wyjść dwumilowymi butami,
#relaksacja wykonuje się 2 razy, dla krawędzi z butami i bez. Złożoność czasowa to O(V^3), a pamięciowa t O(V)

from queue import PriorityQueue
from zad6testy import runtests

def Dijkstra(n, G, G2, start, finish):
    d = [[float('inf'),float('inf')] for _ in range(n)]
    d[start][0] = 0
    d[start][1] = 0
    can_two_mile = True

    Q = PriorityQueue()
    Q.put((0, start, can_two_mile))

    while not Q.empty():
        distance, u, can_two_mile = Q.get()
        if u == finish:
            return distance
        for i in range(n):
            if G[i][u] != 0:
                if relax(Q, d, i, G[i][u], u, False):
                    Q.put((d[i][0], i, True))
        if can_two_mile == True:
            for i in range(n):
                if G2[i][u] != 0:
                    if relax(Q,d, i, G2[i][u], u, True):
                        Q.put((d[i][1], i, False))



def relax(Q,d, v, edge, u, can_two_mile):
    if can_two_mile == True:
        if d[v][1] > d[u][0] + edge:
            d[v][1] = d[u][0] + edge
            return True
    if can_two_mile == False:
        if d[v][0] > d[u][0] + edge:
            d[v][0] = d[u][0] + edge
            Q.put((d[v][0], v, True))
        if d[v][0] > d[u][1] + edge:
            d[v][0] = d[u][1] + edge
            return True
    return False


def jumper(G, s, w):
    n = len(G)
    Gdwa = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if G[i][j] != 0:
                for k in range(0, n):
                    if k != i and G[k][j] != 0:
                        edge = max(G[i][j], G[k][j])
                        if edge < Gdwa[i][k] or Gdwa[i][k] == 0:
                            Gdwa[i][k] = edge
                            #przygotowanie drugiego grafu z krawędziami, które da się przebyć butami
    return (Dijkstra(n, G, Gdwa, s, w))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(jumper, all_tests=True)
