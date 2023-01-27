import sys
  
class Graph():
  
    def __init__(self, vertices):
        self.V, self.graph = vertices, [[0 for column in range(vertices)]for row in range(vertices)]
        
    def calculateMST(self, parent):
        res = 0
        for i in range(1, self.V):
            res = res + (self.graph[i][parent[i]])
        return res
    
    def add_edge(self, u, v, d):
        self.graph[u][v], self.graph[v][u] = d, d
    
    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min, min_index = key[v], v
        return min_index
    
    def primMST(self):
        key, parent, mstSet = [sys.maxsize] * self.V, [None] * self.V, [False] * self.V
        key[0], parent[0] = 0, -1 
        for V in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v], parent[v] = self.graph[u][v], u
        return self.calculateMST(parent)


nm = input().split(" ")
m, n, firstSum= int(nm[1]),int(nm[0]), 0
g = Graph(n)
for i in range(m):
    uvd = input().split(" ")
    g.add_edge(int(uvd[0]),int(uvd[1]),int(uvd[2]))

for row in g.graph:
    for w in row:
        firstSum += w
print((firstSum//2) - g.primMST())