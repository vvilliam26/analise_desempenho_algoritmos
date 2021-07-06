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
        self.v = grafo.v
        self.grafo = grafo

#Regra de heuristica
    def set_heuristica(self, target, start, node):
        #distancia do vertice em analise para o alvo
        dist_target = distancia_euclidiana(self.vertices[target], self.vertices[node])
        #distancia do vertice analisado para o vertice pai
        dist_s = distancia_euclidiana(self.vertices[start], self.vertices[node])
        #heuristca da soma de distancias euclidianas
        dist = dist_target + dist_s
        #retorno dos parametros
        # heuristica = [node, dist, dist_s]
        return dist
        

    from a_element import A_ELEMENT
    def a_estrela(self, end, start):
        distTotal = 0
        visited = [0]*self.v
        visited[start] = True
        pq = PriorityQueue()
        pq.put((0, start))
        anterior = None
        while pq.empty() == False:
            vertice = pq.get()[1]
            if(anterior!=None):
                distTotal += distancia_euclidiana(self.grafo.lista_vertices[anterior], self.grafo.lista_vertices[vertice])
            # Mostrando o caminho de menor custo
            print(vertice, end=" ")
            if vertice == end:
                break
            
            for viz in self.grafo.graph[vertice]:
                if visited[viz] == False:
                    visited[viz] = True
                    pq.put((self.set_heuristics(viz, end), viz))
            anterior = vertice

        print()
        print(distTotal)

            

        


