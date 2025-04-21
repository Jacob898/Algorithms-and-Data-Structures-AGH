#Jakub Stachecki
#Program liczy punkty słabsze w pętli w pętli, jeżeli punkt w pętli ma mniejszy lub równą współrzędną(i nie jest tym punktem) to dodaje go do licznika i liczy maksymalny licznik
# . Złożoność czasowa to O(n^2), a pamięciowa To O(n).

from zad3testy import runtests


from zad3testy import runtests

def dominance(P):
    n = len(P)

    X = [0] * n
    Y = [0] * n

    for i in range(n):
      X[P[i][0] - 1] += 1
    for i in range(n):
      Y[P[i][1] - 1] += 1
    for i in range(n - 2, -1, -1):
      X[i] += X[i + 1]
    for i in range(n - 2, -1, -1):
      Y[i] += Y[i + 1]

    min = 100000000000

    for i in range(n):
      if (X[P[i][0]-1] + Y[P[i][1]-1] < min):
        min = X[P[i][0]-1] + Y[P[i][1]-1]

    return n - min + 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
