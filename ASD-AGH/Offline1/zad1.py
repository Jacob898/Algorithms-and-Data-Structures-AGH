#Jakub Stachecki
#Algorytm polega na posortowaniu linked listy bubble sortem k razy, ponieważ elementy są "oddalone" od docelowego miejsca w
#posortowanej linked liście o maksymalnie k miejsc, a z kolejnymi powtórzeniami bubble sorta te liczby będą się "przybliżać" do miejsca docelowego
# na końcu jest jeszcze zaimplementowany edge case, który zadziała wtedy, gdy będziemy chcieli się odwołać do Node'a który nie istnieje
#Złożoność algorytmu to O(nk), dla k = Θ(1) złożoność to O(n), k = Θ(log n) złożoność to O(n log n)
# oraz dla k = Θ(n) złożoność to O(n^2)
from zad1testy import Node, runtests

def SortH(p, k):
    prev = Node()
    prev.next = p
    start = prev
    for i in range(k):
        prev = start
        p = start.next
        while p.next.next != None:
            if p.val > p.next.val:
                temp = p.next
                p.next = p.next.next
                temp.next = p
                prev.next = temp
            else:
                p = p.next
            prev = prev.next
        if p.val > p.next.val:  # edge case
            temp = p.next
            p.next = None
            temp.next = p
            prev.next = temp
    return start.next
    # tu prosze wpisac wlasna implementacje


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(SortH, all_tests=True)
