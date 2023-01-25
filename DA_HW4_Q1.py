from collections import defaultdict


def add_edge(adj, src, dest, d):
 
    adj[src][dest] = d
    adj[dest][src] = d

# def find_path(adj,s,d):
#     distance = [float('inf')]
#     paths = []
#     priority_queue = {}
#     priority_queue[0] = s
#     distance[s] = 0
#     paths[s] = 1
#     while not priority_queue.empty():
        
    # for i in adj:
    #     if i == start:
    #         for j in adj:
    #             if j == adj[i].keys():
    #                 minPath += adj[i][j]
    #                 if j == end:
    #                     paths.append(minPath)
    #                     return 
    #                 else:
    #                     return find_path(adj,j,end,minPath)
    
nm = input().split(" ")
m, n, paths, adj = int(nm[1]),int(nm[0]), [], defaultdict(dict)
for i in range(m):
    uvd = input().split(" ")
    u, v, d = int(uvd[0]), int(uvd[1]), int(uvd[2])
    add_edge(adj,u,v,d)
find_path(adj, 0, n-1, 0)
minPath, res = min(paths), 0
for i in paths:
    if paths[i] == minPath:
        res += 1
print(res)