#Jakub Stachecki
#algorytm zamienia postać grafu podaną w treści na postać listy odsyłaczowej, przechodzi graf metodą DFS i jeżeli następny punkt spełnia wymagania pułapu(czyli jego różnica z wartością przelotu
#z punktu startowego, najwiekszego i najmniejszego po drodze <= t*2)to do niego przechodzi i sprawdza dalej. Dodatkowo, jeżeli z punktu nie da się
#iść już dalej to trzeba zmienić jego wartość w tablicy Visited na false, ponieważ przez ten punkt może prowadzić inna ścieżka niż ta, w której
#pierwotnie go rozpatrywaliśmy, a która spełnia warunek zadania. Złożoność Czasowa to O(V*E)

from zad4testy import runtests

global_var=0
def DFS_visit(V, x, end, visited, t, p, prev_max, prev_min):
    global global_var
    visited[x] = True
    if x == end:
        global_var = 1
    for u in V[x]:
        if visited[u[0]] == False and abs(u[1] - p) <= t * 2 and abs(u[1] - prev_max) <= t * 2 and abs(u[1] - prev_min) <= t * 2:
            prev_max = max(prev_max, u[1])
            prev_min = min(prev_min, u[1])
            DFS_visit(V, u[0], end, visited, t, p, prev_max, prev_min)

    visited[x] = False



def Flight(L, x, y, t):
    global global_var

    n = max(max(edge[0], edge[1]) for edge in L)
    V = [[] for _ in range(n + 1)]
    for u, v, p in L:
        V[u].append((v, p))
        V[v].append((u, p))
    visited = [False] * len(V)
    visited[x] = True
    end = y
    for u in V[x]:
        p = u[1]
        DFS_visit(V, u[0], end, visited, t, p, p, p)

        if global_var == 1:
            global_var = 0
            return True
    return False

#print(Flight(L,x,y,t))
runtests(Flight, all_tests=True)
