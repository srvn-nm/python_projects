from queue import PriorityQueue


class Node:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight


def add_edge(adj, x, y, d):
 
    adj[x].append(Node(y, d))
    adj[y].append(Node(x, d))
    
def peek(pq):
  return pq.queue[0]

def dijkstra(adj, n, dist, paths):

    pq = PriorityQueue(n + 1)

    settled = set()

    pq.put(Node(0, 0))

    dist[0] = 0
    paths[0] = 1

    while (not pq.empty()) :

        u = peek(pq).node

        d = peek(pq).weight

        pq.get()

        for i in range(len(adj[u])):
            to = adj[u][i].node
            cost = adj[u][i].weight

            if ((str(to) + " " + str(u))in settled):
                continue

            if (dist[to] > dist[u] + cost):

                pq.put(Node(to, (d + cost)))

                dist[to] = dist[u] + cost

                paths[to] = paths[u]
            

            elif (dist[to] == dist[u] + cost) :
                paths[to] = (paths[to] + paths[u])

            settled.add(str(to) + " " + str(u))
        
def findShortestPaths(adj, n) :

        dist = [float('inf')]*(n + 5)

        paths = [0]*(n + 5)

        dijkstra(adj, n, dist, paths)

        print(paths[n])
    
    
nm = input().split(" ")
m, n= int(nm[1]),int(nm[0])
adj = [[]for i in range(n)]

for i in range(m):
    uvd = input().split(" ")
    u, v, d = int(uvd[0]), int(uvd[1]), int(uvd[2])
    add_edge(adj,u,v,d)

findShortestPaths(adj, n-1)