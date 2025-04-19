def counting_sort_word(A,letter, k=26):
    n = len(A)
    B = [None] * n
    C = [0] * k

    for x in range(n):
        C[ord(A[x][letter])-ord('a')] += 1
    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):  # range(0, n)[::-1]
        B[C[ord(A[i][letter])-ord('a')] - 1] = A[i]
        C[ord(A[i][letter])-ord('a')] -= 1

    for i in range(n):
        A[i]=B[i]
    return A
T=["kra","art","kot","kit","ati","kil"]
for i in range(2,-1,-1):
    counting_sort_word(T,i)
print(T)
