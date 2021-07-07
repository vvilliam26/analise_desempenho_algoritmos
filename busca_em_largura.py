
class BFS:

    # def __init__(self, grafo_knn):
    #     self.graph = grafo_knn

    #constroi a função que ira criar a lista 
    def __init__(self, grafo_knn): 
        self.graph = grafo_knn.graph

    #recebe start e target
    def bfs(self, start, end):

        visited = []

        queue = [[start]]

        if start== end:
            return "Start = Target"

        while queue:
            #pop no elemento a ser analisado na fila
            caminhos = queue.pop(0)
            # print(s, " ")

            vertice = caminhos[-1]
            if vertice not in visited:
                vizinhos = self.graph[vertice]
                for vizinho in vizinhos:
                    novo_caminho = list(caminhos)
                    novo_caminho.append(vizinho)
                    queue.append(novo_caminho)

                    if vizinho == end:
                        #print("Caminho BFS: %s" %(novo_caminho))
                        #print("Distancia BFS: %s")
                        return novo_caminho
                visited.append(vertice)
    

    # def addEdge(self,u,v): 
    #     self.graph[u].append(v) 