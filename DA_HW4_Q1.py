from queue import PriorityQueue


class Node:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight


def add_edge(adj, x, y, d):
 
    adj[x].append(Node(y, d))
    adj[y].append(Node(x, d))

def dijkstra(adj, n, dist, paths):

    pq = PriorityQueue<Node>(n + 1, Node())

    settled = set()

    pq.add(Node(0, 0))

    dist[0] = 0
    paths[0] = 1

    while (not pq.isEmpty()) :

        u = pq.peek().node

        d = pq.peek().weight

        pq.poll()

        for i in range(adj.get(u).size()):
            to = adj.get(u).get(i).node
            cost = adj.get(u).get(i).weight

            if (settled.contains(to + " " + u)):
                continue

            if (dist[to] > dist[u] + cost):

                pq.add(Node(to, d + cost))

                dist[to] = dist[u] + cost

                paths[to] = paths[u]
            

            elif (dist[to] == dist[u] + cost) :
                paths[to] = (paths[to] + paths[u])

            settled.add(to + " " + u)
        
def findShortestPaths(adj, n) :

        dist = []*(n + 5)

        paths = []*(n + 5)

        for i in range(n+1):
            dist[i] = int.MAX_VALUE

        for i in range(n+1):
            paths[i] = 0

        dijkstra(adj, n, dist, paths)

        print(paths[n])
    
    
nm = input().split(" ")
m, n= int(nm[1]),int(nm[0])
adj = [[]*n]

for i in range(m):
    uvd = input().split(" ")
    u, v, d = int(uvd[0]), int(uvd[1]), int(uvd[2])
    add_edge(adj,u,v,d)

findShortestPaths(adj, n-1)