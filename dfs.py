from collections import defaultdict
from math import sqrt

def distancia_euclidiana(x1, x2):
    return sqrt(((x1[0]-x2[0])**2+(x1[1]-x2[1])**2))
 
class DFS:
    # Constructor
    def __init__(self, grafo_knn):
        self.set_grafo(grafo_knn)


    def set_grafo(self, grafo_knn):
        self.grafo = grafo_knn
 
    # function to add an edge to graph
 
    # A function used by DFS
    def DFSUtil(self, v, target, visited, path, prev):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)

        if(prev!=None):
            self.dist+=distancia_euclidiana(self.grafo.lista_vertices[prev], self.grafo.lista_vertices[v])
            
        #print(v, end=' ')
        if(v == target):
            path.append(v)
            return True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.grafo.graph[v]:
            if neighbour not in visited:
                prev = v
                if self.DFSUtil(neighbour, target, visited, path, prev) == True:
                    path.append(v)
                    return True


        if(self.dist>0):
            self.dist -= distancia_euclidiana(self.grafo.lista_vertices[prev], self.grafo.lista_vertices[v])

        return False
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v, target):
 
        # Create a set to store visited vertices
        visited = set()

        #Lista que armazena o caminho atual
        path = list()
        self.dist = 0.0
        prev = None
        # Call the recursive helper function
        # to print DFS traversal
        if(self.DFSUtil(v,target, visited, path, prev)==True):
            print(path[::-1])
            print(self.dist)
        else:
            print("Erro, caminho nao encontrado")
        