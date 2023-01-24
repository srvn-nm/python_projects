from collections import defaultdict


# def add_edge(adj, src, dest, d):
# 
#     adj[src][dest] = d
#     adj[dest][src] = d

# def find_path(adj,start,end,minPath):
# 
#     for i in adj:
#         if i == start:
#             for j in adj:
#                 if j == adj[i].keys():
#                     minPath += adj[i][j]
#                     if j == end:
#                         paths.append(minPath)
#                         return 
#                     else:
#                         return find_path(adj,j,end,minPath)


class Graph:
  
    def __init__(self,vertices):
        self.V = vertices 
        self.V_org = vertices
        self.shortestPaths = []
        self.graph = defaultdict(list) # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        if w == 1:
            self.graph[u].append(v)
        else:   
            '''split all edges of weight 2 into two
            edges of weight 1 each.  The intermediate
            vertex number is maximum vertex number + 1,
            that is V.'''
            self.graph[u].append(self.V)
            self.graph[self.V].append(v)
            self.path = []
            self.V = self.V + 1
     
    # To find the shortest path stored in parent[]
    def Path(self, parent, j):
        Path_len = 1
        if parent[j] == -1 and j < self.V_org : #Base Case : If j is source
            self.path.append(j)
            return 0 # when parent[-1] then path length = 0   
        l = self.Path(parent , parent[j])
 
        #increment path length
        Path_len = l + Path_len

        if j < self.V_org :
            self.path.append(j)
 
        return Path_len
 
    '''This function mainly does BFS and prints the
        shortest path from src to dest. It is assumed
        that weight of every edge is 1'''
    def findShortestPath(self,src, dest):
 
        # Mark all the vertices as not visited
        # Initialize parent[] and visited[]
        visited =[False]*(self.V)
        parent =[-1]*(self.V)
  
        # Create a queue for BFS
        queue=[]
  
        # Mark the source node as visited and enqueue it
        queue.append(src)
        visited[src] = True
  
        while queue :
             
            # Dequeue a vertex from queue
            s = queue.pop(0)
             
            # if s = dest then print the path and return
            if s == dest:
                self.shortestPaths.append(self.Path(parent, s))
                 
  
            # Get all adjacent vertices of the dequeued vertex s
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = s
            
    
nm = input().split(" ")
m, n= int(nm[1]),int(nm[0])
g = Graph(n)
for i in range(m):
    uvd = input().split(" ")
    u, v, d = int(uvd[0]), int(uvd[1]), int(uvd[2])
    g.addEdge(u,v,d)
g.findShortestPath(0, n-1)
print(len(g.shortestPaths))