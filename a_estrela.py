from a_element import A_ELEMENT
from math import sqrt
import math
from collections import defaultdict


def distancia_euclidiana(x1, x2):
    distancia = 0.0
    if x1 == x2:
        return distancia
    for i in range(len(x1)):
        distancia += (x1[i] - x2[i])**2
    return sqrt(distancia)

class A_ESTRELA:

#O grafo em modo de dicionário deve ser passado para inicializar o A*
    def __init__(self, v, grafo_arestas, grafo_vertices) -> None:
        #setando o infinito
        self.INF = math.inf
        #numero de vertices
        self.v = v
        self.graph = grafo_arestas
        self.vertices = grafo_vertices

#Regra de heuristica
    def set_heuristica(self, target, start, node):
        #distancia do vertice em analise para o alvo
        dist_target = distancia_euclidiana(self.vertices[target], self.vertices[node])
        #distancia do vertice analisado para o vertice pai
        dist_s = distancia_euclidiana(self.vertices[start], self.vertices[node])
        #heuristca da soma de distancias euclidianas
        dist = dist_target + dist_s
        #retorno dos parametros
        heuristica = [node, dist, dist_s]
        return heuristica
        

    from a_element import A_ELEMENT
    def a_estrela(self,s, t):
        #vertice analisado ou start
        vertice = s
        #a element eh um objeto que armazena o caminho e a distancia
        caminho = A_ELEMENT(vertice, 0)
        for i in range(self.v*100):
            vizinhos = self.graph[vertice]
            dist = self.INF
            #para todos os vizinhos do no pai
            for vizinho in vizinhos:
                #defininado os parametros do vertice
                h = self.set_heuristica(t, vertice, vizinho)
                #armazenando o melhor no segundo a heuristica definida
                if h[1] < dist and caminho.isVisitado(h[0]) == False:
                    h_min = h
                    dist = h_min[1]
            if caminho.isVisitado(h_min[0]) == True:
                print("Não existe caminho entre os dois vértices.")
                break
            caminho.add_vertice(h_min[0])
            caminho.add_distance(h_min[2])
            print(caminho.path)
            if(h_min[0] == t):
                print(caminho.path)
                print(caminho.distance_sum)
                break
            vertice = h_min[0]
        return caminho
            

        


