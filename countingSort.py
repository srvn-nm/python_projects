def countingSort(A,n,k):
    c = [0 for i in range(k+1)] 
    B = [0 for i in range(n)] 
    for i in range(n):
        c[A[i]] += 1
    for i in range(k+1):
        c[i] += c[i-1]
    for i in range(n-1,0,-1):
        B[c[A[i]] - 1] = A[i]
        c[A[i]] -= 1
    return B


A=[0,9,8,4,0,9,2,5]
print(countingSort(A,len(A),9))