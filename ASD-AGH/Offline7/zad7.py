#Jakub Stachecki
#Algorytm polega na przechodzeniu najpierw w dół(kiedy to porównuje się wartość z lewej i z góry) oraz w górę tej samej kolumny niezależnie,
#na koniec wartość w odpowiedniej kolumnie tablicy costs_left ustawia się na maksymalne wartości przechodzenia z góry i z dołu
#złożoność czasowa to O(n^2), a pamięciowa to O(3n^2)
from zad7testy import runtests


def maze(L):
    n = len(L)
    costs_down = [[0 for _ in range(n)] for _ in range(n)]
    costs_up = [[0 for _ in range(n)] for _ in range(n)]
    costs_left = [[0 for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if L[y][x] == "#":
                costs_down[y][x] = -float("inf")
                costs_up[y][x] = -float("inf")
                costs_left[y][x] = -float("inf")

    for y in range(1, n):
        costs_down[y][0] += costs_down[y - 1][0] + 1
        costs_up[y][0] = - float("inf")  #idąc tylko do góry nigdy się nie dostaniemy do kolumny 0
        costs_left[y][0] = costs_down[y][0]

    for x in range(1, n):

        for y in range(n): #chodzenie do dołu
            if L[y][x] != "#":
                if y == 0:
                    costs_down[0][x] = costs_left[0][x - 1] + 1
                else:
                    costs_down[y][x] = max(costs_down[y - 1][x], costs_left[y][x - 1]) + 1

        for y in range(n - 1, -1, -1):  #chodzenie do góry
            if L[y][x] != "#":
                if y == n - 1:
                    costs_up[n - 1][x] = costs_left[n - 1][x - 1] + 1
                else:
                    costs_up[y][x] = max(costs_up[y + 1][x], costs_left[y][x - 1]) + 1

        for y in range(n):
            costs_left[y][x] = max(costs_down[y][x], costs_up[y][x])

    if costs_left[n - 1][n - 1] != -float("inf"):
        return costs_left[n - 1][n - 1]
    return -1


runtests(maze, all_tests=True)
