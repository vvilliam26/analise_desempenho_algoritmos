from collections import defaultdict
from math import dist, sqrt
from knn import KNN
from queue import PriorityQueue



def distancia_euclidiana(x1, x2):
    return sqrt(((x1[0]-x2[0])**2+(x1[1]-x2[1])**2))


class A_DEF:
    # Constructor
    def __init__(self, grafo_knn):
        self.grafo = (grafo_knn)
        
    #Calcula o F(v) para um dado vertice v (ja soma g(v) e h(v))
    def heuristics(self,start, atual, end):
        return (distancia_euclidiana(self.grafo.lista_vertices[atual],
        self.grafo.lista_vertices[end])*10)+distancia_euclidiana(self.grafo.lista_vertices[start],
        self.grafo.lista_vertices[atual])
    
    #O algoritmo usado aqui eh o mesmo da busca informada,
    #em caso de duvida ve o algoritmo comentado la.
    #A unica coisa que muda entre best 1st, A e A* eh a heuristica
    def algoA(self, start, end):
        path = list()
        distTotal = 0
        visited = [0]*self.grafo.v
        visited[start] = True
        pq = PriorityQueue()
        pq.put((0, start))
        anterior = None
        while pq.empty() == False:
            vertice = pq.get()[1]
            if(anterior!=None):
                distTotal += distancia_euclidiana(self.grafo.lista_vertices[anterior], self.grafo.lista_vertices[vertice])
            # Mostrando o caminho de menor custo
            path.append(vertice)
            if vertice == end:
                break
            
            for viz in self.grafo.graph[vertice]:
                if visited[viz] == False:
                    visited[viz] = True
                    pq.put((self.heuristics(start, viz, end), viz))
            anterior = vertice

        if(vertice == end):
            path.reverse()

            return distTotal
        # else: