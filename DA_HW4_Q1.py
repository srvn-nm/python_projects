def add_edge(adj, src, dest, d):
 
    adj[src][dest] = d
    adj[dest][src] = d

paths=[]
def find_path(adj,start,end,minPath):
    
    for i in adj:
        if i == start:
            for j in adj:
                if j == adj[i].keys():
                    minPath += adj[i][j]
                    if j == end:
                        paths.append(minPath)
                        return 
                    else:
                        return find_path(adj,j,end,minPath)
    
mn = input()
m = int(mn[2])
n = int(mn[0])
adj = [{} for i in range(n)]
for i in range(m):
    uvd = input()
    u = int(uvd[0])
    v = int(uvd[2])
    d = int(uvd[4])
    add_edge(adj,u,v,d)
find_path(adj, 0, n-1, 0)
minPath = min(paths)
res = 0
for i in paths:
    if paths[i] == minPath:
        res += 1
print(res)