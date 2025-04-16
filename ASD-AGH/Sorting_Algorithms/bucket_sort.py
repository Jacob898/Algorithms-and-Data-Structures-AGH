

def bucket_sort(T):
    n=T[0]
    l=len(T)
    for i in range(l):
        if(T[i]>n):
            n=T[i]
    #print(max(T))

    buckets=[[]for _ in range(l+1)]

    for x in T:
        i=((x/n)*l)
        buckets[int(i)].append(x)

    result=[]
    for bucket in buckets:
        if bucket:
            sorted(bucket)
        for x in bucket:
            result.append(x)

    return result


