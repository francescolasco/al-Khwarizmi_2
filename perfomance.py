from Graph_IncidenceList_MOD import *
from random import randint

def generateWeightedGraph(numNodes):
    graph = GraphIncidenceList()
    nodes = []

    graph.print()

    for i in range(numNodes):
        node = graph.addNode(i, randint(1, numNodes))
        nodes.append(node)

    for node_src in nodes:
        for node_dst in nodes:
            if node_src != node_dst:
                print("---")
                print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id, graph.isAdj(node_src.id, node_dst.id)))
                graph.insertEdge(node_src.id, node_dst.id, node_src.id + node_dst.id)
                print("Edge inserted: from {} to {}".format(node_src.id, node_dst.id))
                print("Adjacent nodes {},{}: {}".format(node_src.id, node_dst.id, graph.isAdj(node_src.id, node_dst.id)))
                graph.print()
                print("---")
    print("Num Nodes:", graph.numNodes())
    print("Num Edges:", graph.numEdges())
    graph.print()