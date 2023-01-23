from collections import defaultdict


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
    
nm = input().split(" ")
m, n = int(nm[1]),int(nm[0])
adj = defaultdict(dict)
for i in range(m):
    uvd = input().split(" ")
    u, v, d = int(uvd[0]), int(uvd[1]), int(uvd[1])
    add_edge(adj,u,v,d)
find_path(adj, 0, n-1, 0)
minPath, res = min(paths), 0
for i in paths:
    if paths[i] == minPath:
        res += 1
print(res)