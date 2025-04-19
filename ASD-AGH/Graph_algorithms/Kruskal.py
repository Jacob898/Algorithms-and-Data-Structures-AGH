class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(E, n):
    A = []
    E.sort(key=lambda x: x[2])
    #MergeSort(E)
    V = [Node(i) for i in range(n)]

    for e in E:
        u, v, w = e
        if find(V[u]) != find(V[v]):
            union(V[u], V[v])
            A += [e]
    return A


def MergeSort(A):
    n = len(A)
    if n > 1:
        i = n // 2
        L = A[:i]
        R = A[i:]
        MergeSort(L)
        MergeSort(R)
        j = k = 0
        while j < i and k < n - i:
            if L[j][2] <= R[k][2]:
                A[j + k] = L[j]
                j += 1
            else:
                A[j + k] = R[k]
                k += 1
        while j < i:
            A[j + k] = L[j]
            j += 1
        while k < n - i:
            A[j + k] = R[k]
            k += 1


E = [(0, 1, 1), (0, 4, 5), (0, 5, 8), (1, 0, 1), (1, 2, 3), (2, 1, 3), (2, 3, 6), (2, 4, 4),
     (3, 2, 6), (3, 4, 2), (4, 0, 5), (4, 2, 4), (4, 3, 2), (4, 5, 7), (5, 0, 8), (5, 4, 7)]
print(kruskal(E, 6))

#minimalny cykl w grafie
#usuwamy krawędź, idziemy do niej inaczej a później ją dodajemy
#w grafie skierowanym robimy ją w dwie strony
