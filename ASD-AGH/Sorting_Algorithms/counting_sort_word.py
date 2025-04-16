def counting_sort_word(A,k=27):
    n = len(A)
    B = [None] * n
    C = [0] * k

    for x in range(0,len(A)):
        C[ord(A[x])-ord('a')] += 1
    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):  # range(0, n)[::-1]
        B[C[ord(A[i])-ord('a')] - 1] = A[i]
        C[ord(A[i])-ord('a')] -= 1

    return B


T = "testing"
print(counting_sort_word(T))
