def minSteps(str):
    n = len(str)
    res= [[0]*(n+1)]*(n+1)
    for l in range(1,n+1):
        i = 0
        for j in range(l-1,n+1):
            if l == 1:
                res[i][j] = 1
            else:
                res[i][j] = 1 + res[i+1][j]
                if str[i] == str[i+1]:
                    res[i][j] = min(1 + res[i+2][j], res[i][j])
                for k in range(i+2, j+1):
                    if str[i] == str[k]:
                         res[i][j] = min(res[i+1][k-1] + res[k+1][j], res[i][j])
        i += 1
    print(res[0][n-1])


minSteps(input())