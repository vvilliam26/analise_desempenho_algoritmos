from collections import defaultdict
from math import sqrt
from sys import setrecursionlimit

setrecursionlimit(500000)

def distancia_euclidiana(x1, x2):
    sum = 0
    for i in range (0,1):
        sum+=(x1[i]+x2[i])**2
    return sqrt(sum)
 
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
    def DFS(self, start, end):
 
        # Create a set to store visited vertices
        visited = set()

        #Lista que armazena o caminho atual
        path = list()
        self.dist = 0.0
        prev = None
        # Call the recursive helper function
        # to print DFS traversal
        if(self.DFSUtil(start,end, visited, path, prev)==True):
            path.reverse()
            #print("Caminho DFS: %s" %(path))
            #print("Distancia DFS: %s" % (self.dist))
            return path
        #else:
            #print("Erro, caminho nao encontrado")
        