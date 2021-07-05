from collections import defaultdict

class BFS:

    def __init__(self, grafo_knn):
        self.graph = self.set_grafo(grafo_knn)


    def set_grafo(self, grafo_knn):
        self.graph = defaultdict(list)
        
        for vertice in grafo_knn:
            for u in range(len(vertice)-1):
                self.graph[vertice[0]].append(vertice[u+1])
        print (self.graph)
    