from collections import defaultdict
from math import sqrt
from knn import KNN
from queue import PriorityQueue



def distancia_euclidiana(x1, x2):
    return sqrt(((x1[0]-x2[0])**2+(x1[1]-x2[1])**2))


class Best1st:
    # Recebe o grafo e o torna parte dessa classe
    def __init__(self, grafo_knn):
        self.grafo = (grafo_knn)
        
    #Calcula o F(v) para um dado vertice v (usando heuristica de 
    #distancia ao no final)
    def heuristics(self, atual, end):
        return (distancia_euclidiana(self.grafo.lista_vertices[atual], self.grafo.lista_vertices[end]))

    #Algoritmo de busca informada iterativo
    def bestFirstSearch(self, start, end):
        #Inicializando variáveis úteis
        path = list()
        distTotal = 0
        visited = [0]* self.grafo.v
        visited[start] = True
        #Inicializa a priority queue
        pq = PriorityQueue()
        pq.put((0, start))#insere o no inicial
        anterior = None#para calcular distancia

        while pq.empty() == False:
            vertice = pq.get()[1]#puxa sempre o no de menor custo da priority queue, inicialmente pega o start
            #soma a distancia do anterior ao atual, a nao ser que seja o start
            if(anterior!=None):
                distTotal += distancia_euclidiana(self.grafo.lista_vertices[anterior], self.grafo.lista_vertices[vertice])
            # Mostrando o caminho de menor custo
            path.append(vertice)
            if vertice == end:
                break
            #Bota os nos vizinhos do certice na priority queue,
            #caso nao tenham sido visitados
            for viz in self.grafo.graph[vertice]:
                if visited[viz] == False:
                    visited[viz] = True
                    pq.put((self.heuristics(viz, end), viz))
            anterior = vertice
        #retorna o caminho, caso tenha sido encontrado
        if(vertice == end):
            path.reverse()
            return distTotal


