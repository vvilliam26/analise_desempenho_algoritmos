from igraph import *

eG=Graph()
eG.add_vertices(6)
eG.add_edges([(0,1),(1,2),(2,3),(3,4),(3,5),(5,3)])
# eG.es['weight']=[12,1,2,3,4,1]

layout = eG.layout("kk")

# visual_style = {}
# visual_style["vertex_size"] = 20
# visual_style["vertex_label"] = ["a","b","c","d","e","f"]
# visual_style["edge_width"] = eG.es['weight']
# visual_style["bbox"] = (300, 300)


plot(eG)