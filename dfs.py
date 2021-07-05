from collections import defaultdict

 
class DFS:
    # Constructor
    def __init__(self, grafo_knn):
        self.set_grafo(grafo_knn)


    def set_grafo(self, grafo_knn):
        self.graph = defaultdict(list)
        
        for vertice in grafo_knn:
            for u in range(len(vertice)-1):
                self.graph[vertice[0]].append(vertice[u+1])
 
    # function to add an edge to graph
 
    # A function used by DFS
    def DFSUtil(self, v, target, visited, path):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)

        #Insert currend node into path, will remove at the end
        #of the function call
        path.append(v)
        #print(v, end=' ')
        if(v == target):
            return True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                    if self.DFSUtil(neighbour, target, visited, path) == True:
                        return True
        path.pop()
        return False
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v, target):
 
        # Create a set to store visited vertices
        visited = set()

        #Lista que armazena o caminho atual
        path = list()
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v,target, visited, path)
        if(len(path)>=1):
            print(path)
