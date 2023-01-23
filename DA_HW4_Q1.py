def add_edge(adj, src, dest, d):
 
    adj[src][dest] = d
    adj[dest][src] = d
    
    
    
mn = input()
m = int(mn[0])
n = int(mn[2])
adj = [{} for i in range(n)]
for i in range(m):
    uvd = input()
    u = int(uvd[0])
    v = int(uvd[2])
    d = int(uvd[4])
    add_edge(adj,u,v,d)
