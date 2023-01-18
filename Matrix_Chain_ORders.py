def matrixChainOrder(p):
    n = len(p) - 1
    m = [[0]*(n-1)]*(n-1)
    s = [[0]*(n-2)]*(n-2)
    for l in range(2,n+1):
        for i in range(1,n-l):
            j = i+l-1
            m[i][j] = float('inf')
            for k in range(i, j-1):
                q=m[i][k]+m[k+1][j]+(p[i-1]*p[k]*p[j])
                if q< m[i][j]:
                    m[i][j] = q
                    s[i][j] = k    
    return m,s
    
def printOptimal(s,i,j):
    if i==j:
        print("A"+str(i))
    else:
        print("(")
        printOptimal(s,i,s[i][j])
        printOptimal(s,s[i][j]+1,j)
        print(")")
        
p=[5,2,3,4,6]
(m,s) = matrixChainOrder(p)
printOptimal(s,0,len(p)-2)

