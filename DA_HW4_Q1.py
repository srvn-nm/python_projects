from queue import PriorityQueue


class Node:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight
    
    def __eq__(self, other):
        return (self.node == other.node) and (self.weight == other.weight)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.node < other.node) and (self.weight < other.weight)

    def __gt__(self, other):
        return (self.node > other.node) and (self.weight > other.weight)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)


def add_edge(adj, x, y, d):
 
    adj[x].append(Node(y, d))
    adj[y].append(Node(x, d))
    
def peek(pq):
  return pq.queue[0]

def dijkstra(adj, n, dist, paths):

    pq, settled, dist[0], paths[0] = PriorityQueue(n + 1), set(), 1

    pq.put(Node(0, 0))

    while (not pq.empty()) :

        u, d = peek(pq).node, peek(pq).weight

        pq.get()

        for i in range(len(adj[u])):
            to, cost = adj[u][i].node, adj[u][i].weight

            if ((str(to) + " " + str(u)) in settled):
                continue

            if (dist[to] > dist[u] + cost):

                pq.put(Node(to, (d + cost)))

                dist[to], paths[to] = (dist[u] + cost), paths[u]
            

            elif (dist[to] == dist[u] + cost) :
                paths[to] = (paths[to] + paths[u])

            settled.add(str(to) + " " + str(u))
        
def findShortestPaths(adj, n) :

        dist, paths = [float('inf')]*(n + 5), [0]*(n + 5)

        dijkstra(adj, n, dist, paths)

        print(paths[n])
    
    
nm = input().split(" ")
m, n= int(nm[1]),int(nm[0])
adj = [[]for i in range(n)]

for i in range(m):
    uvd = input().split(" ")
    add_edge(adj,int(uvd[0]),int(uvd[1]),int(uvd[2]))

findShortestPaths(adj, n-1)