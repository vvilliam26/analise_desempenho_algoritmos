
from a_estrela import distancia_euclidiana


class BFS:

    #constroi a função que ira criar a lista 
    def __init__(self, grafo_knn): 
        self.grafo = grafo_knn

    #recebe start e target
    def bfs(self, start, end):

        #array de visitados
        visited = []
        queue = [[start]] #fila de vertices a serem visitados

        if start== end:
            return "Start = Target"

        while queue:
            caminhos = queue.pop(0)

            vertice = caminhos[-1]
            if vertice not in visited:
                vizinhos = self.grafo.graph[vertice]
                for vizinho in vizinhos:
                    novo_caminho = list(caminhos)
                    novo_caminho.append(vizinho)
                    queue.append(novo_caminho)

                    if vizinho == end:
                        # print("Caminho BFS: %s" %(novo_caminho))
                        distTotal = self.calcula_distancia(novo_caminho)
                        return distTotal
                        #return distTotal
                visited.append(vertice)
    
    def calcula_distancia(self, path):
        coords = self.grafo.lista_vertices
        dist = 0
        for vertice in path:
            if(vertice - 1 > 0):
                dist += distancia_euclidiana(coords[vertice], coords[vertice - 1])
        return dist



