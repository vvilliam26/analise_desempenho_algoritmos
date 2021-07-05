from djk_element import DJK_ELEMENT
from math import sqrt
import math
from collections import defaultdict


def distancia_euclidiana(x1, x2):
    distancia = 0.0
    for i in range(len(x1)):
        distancia += (x1[i] - x2[i])**2
    return sqrt(distancia)

class DIJKSTRA:

#O grafo em modo de dicionário deve ser passado para inicializar o A*
    def __init__(self, v, grafo_knn) -> None:
        #setando o infinito
        self.INF = math.inf
        #numero de vertices
        self.v = v
        self.graph = grafo_knn

#Regra de heuristica
    def set_heuristica(self, target, start, node):
        #distancia do vertice em analise para o alvo
        dist_target = distancia_euclidiana(self.graph[target], self.graph[node])
        #distancia do vertice analisado para o vertice pai
        dist_s = distancia_euclidiana(self.graph[start], self.graph[node])
        #heuristca da soma
        dist = dist_target + dist_s
        #retorno dos parametros
        heuristica = [node, dist, dist_s]
        return heuristica
        

    from djk_element import DJK_ELEMENT
    def dijkstra(self,s, t):
        #vertice analisado ou start
        vertice = s
        #djk element eh um objeto que armazena o caminho e a distancia
        caminho = DJK_ELEMENT(vertice, 0)
        for i in range(self.v - 1):
            vizinhos = self.graph[vertice]
            dist = self.INF
            #para todos os vizinhos do no pai
            for vizinho in vizinhos:
                #defininado os parametros do vertice
                h = self.set_heuristica(t, vertice, vizinho)
                #armazenando o melhor no segundo a heuristica definida
                if h[1] < dist:
                    h_min = h
            caminho.add_vertice(h_min[0])
            caminho.add_distance(h_min[2])
            if(h_min[0] == t):
                break
            vertice = h_min[0]
        return caminho
            

        


