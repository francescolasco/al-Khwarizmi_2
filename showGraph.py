from priorityQueue.PQ_Dheap import PQ_DHeap
from priorityQueue.PQbinaryHeap import PQbinaryHeap
from Graph_IncidenceList_prioritySearch import *
from random import *
import networkx 
import matplotlib.pyplot as plt

#Script per disegno di grafi da inserire in relazione.

def prioritySearchDraw(graph):
    """
    Implementazione modificata di visitaInPriorita' 
    (implementata con binary heap),
    converte il grafo nella struttura Graph della libreria 
    networkx e crea un set di immagini del grafo, tramite
    la libreria matplotlib, evidenziando passo passo i nodi visitati.
    """

    edges = graph.getEdges()
    nodes = graph.getNodes()

    name  = 'graphPictures/figure'
    name_n = 0

    edgeCouples = []
    nodesID = []

    for edge in edges:
        edgeCouples.append((edge.head, edge.tail))

    for node in nodes:
        nodesID.append(node.id)
    
    G = networkx.Graph()
    for nodeID in nodesID:
        G.add_node(nodeID, w = (graph.getNode(0)).getWeight())
    G.add_edges_from(edgeCouples)
    
    labels = dict.fromkeys(nodesID, 0)
    for key in labels.keys():
        labels[key] = graph.nodes[key].getWeight()
    
    pos = networkx.spring_layout(G)

    networkx.draw_networkx(G, pos, arrows = True, with_labels = True, node_size = 500, labels = labels) 
    
    plt.axis('off')
    outputName = name + str(name_n) + ' .png'
    plt.savefig(outputName)
    name_n += 1

    pq = PQbinaryHeap()
    exploredNodes = []

    s = graph.maxWeight()
    ID = s[0]
    KEY = -(s[1])
    pq.insert(ID, KEY)

    while not pq.isEmpty():
        u = pq.findMin()
        pq.deleteMin()

        exploredNodes.append(u)
        networkx.draw_networkx(G, pos, arrows = True, with_labels = True, node_size = 500, labels = labels)
        networkx.draw_networkx_nodes(G, pos, nodelist = exploredNodes, node_color = 'b', node_size = 500)
        
        plt.axis('off')
        outputName = name + str(name_n) + ' .png'
        plt.savefig(outputName)
        name_n += 1

        for vertex in graph.getAdj(u):
            ID = vertex
            KEY = -(graph.getNodes()[vertex].getWeight())
            if ID not in exploredNodes:
                pq.insert(ID, KEY)

    return exploredNodes

def main():
    g = buildGraph(10)
    exploredNodes = prioritySearchDraw(g)
    print('explored nodes: ' + str(exploredNodes))
    print('Done.')

main()