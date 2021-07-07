from math import sqrt
from queue import PriorityQueue



def distancia_euclidiana(x1, x2):
    distancia = 0.0
    if x1 == x2:
        return distancia
    for i in range(len(x1)):
        distancia += (x1[i] - x2[i])**2
    return sqrt(distancia)

class A_ESTRELA:

#O grafo em modo de dicionário deve ser passado para inicializar o A*
    def __init__(self, grafo) -> None:
        #setando o infinito
        #numero de vertices
        self.grafo = grafo

#Regra de heuristica
    def set_heuristica(self, target, start, node):
        #distancia do vertice em analise para o alvo
        dist_target = distancia_euclidiana(self.grafo.lista_vertices[target], self.grafo.lista_vertices[node])
        #distancia do vertice analisado para o vertice pai
        dist_s = distancia_euclidiana(self.grafo.lista_vertices[start], self.grafo.lista_vertices[node])
        #heuristca da soma de distancias euclidianas
        dist = dist_target + dist_s

        return dist
        

    def a_estrela(self, start, end, n):
        path = list()
        distTotal = 0
        visited = [0]*n
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
                    pq.put((self.set_heuristica(end, vertice, viz), viz))
            anterior = vertice

        if(vertice == end):
            path.reverse()          

            return path


            

        


