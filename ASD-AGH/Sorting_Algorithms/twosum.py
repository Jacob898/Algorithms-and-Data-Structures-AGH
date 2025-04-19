
def hasArrayTwoCandidates(A, arr_size, sum):
    # sort the array
    l = 0
    r = arr_size-1

    # traverse the array for the two elements
    while l < r:
        if (A[r] - A[l] == sum):
            return 1
        elif (A[r] - A[l] < sum):
            l += 1
        else:
            r -= 1
    return 0

A = [-8, 1, 4, 6, 10, 45]
n = 2
if (hasArrayTwoCandidates(A, len(A), n)):
    print("Yes")
else:
    print("No")