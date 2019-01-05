from priorityQueue.PQ_Dheap import PQ_DHeap
from priorityQueue.PQbinaryHeap import PQbinaryHeap
from priorityQueue.PQbinomialHeap import PQbinomialHeap
from Graph_IncidenceList_MOD import GraphIncidenceList
from graph.Graph import *
from random import *

class GraphIL_prioritySearch(GraphIncidenceList):
    
        def __init__(self):
            """
            Constructor.
            """
            super().__init__()


        def prioritySearch_PQbinaryHeap(self):
            """
            This algorithm executes a prioritySearch based on the genericSearch of a graph. 
            It uses a list to represent the visit of the graph and a Binary Heap as priority queue for the nodes to explore.
            :param graph: a graph to explore.
            :return: the list of the exploration.
            """
            pq = PQbinaryHeap()
            exploredNodes = []

            s = self.maxWeight()
            ID = s[0]
            KEY = -(s[1])
            pq.insert(ID, KEY)

            while not pq.isEmpty():
                u = pq.findMin()
                pq.deleteMin()

                exploredNodes.append(u)
                
                for ID in self.getAdj(u):
                    node = self.getNode(ID)
                    KEY = -(node.getWeight())
                    if ID not in exploredNodes:
                        pq.insert(ID, KEY)

            return exploredNodes


        def prioritySearch_PQbinomialHeap(self):
            """
            This algorithm executes a prioritySearch based on the genericSearch of a graph. 
            It uses a list to represent the visit of the graph and a Binomial Heap as priority queue for the nodes to explore.
            :param graph: a graph to explore.
            :return: the list of the exploration.
            """
            pq = PQbinomialHeap()
            exploredNodes = []

            s = self.maxWeight()
            ID = s[0]
            KEY = -(s[1])
            pq.insert(ID, KEY)

            while not pq.isEmpty():
                u = pq.findMin()
                pq.deleteMin()

                exploredNodes.append(u)
                
                for ID in self.getAdj(u):
                    node = self.getNode(ID)
                    KEY = -(node.getWeight())
                    if ID not in exploredNodes:
                        pq.insert(ID, KEY)

            return exploredNodes


        def prioritySearch_PQ_DHeap(self, d):
            """
            This algorithm executes a prioritySearch based on the genericSearch of a graph. 
            It uses a list to represent the visit of the graph and a D-Heap as priority queue for the nodes to explore.
            :param graph: a graph to explore.
            :return: the list of the exploration.
            """
            assert d >= 1, "spippettone"
            pq = PQ_DHeap(d)
            exploredNodes = []

            s = self.maxWeight()
            ID = s[0]
            KEY = -(s[1])
            pq.insert(ID, KEY)

            while not pq.isEmpty():
                u = pq.findMin()
                pq.deleteMin()

                exploredNodes.append(u)
                
                for ID in self.getAdj(u):
                    node = self.getNode(ID)
                    KEY = -(node.getWeight())
                    if ID not in exploredNodes:
                        pq.insert(ID, KEY)

            return exploredNodes


def buildGraph(nVertices):
    """
    build a Graph ready for prioritySearch()
    using random weights and random edges 
    between vertices.
    The graph will have as may edges as 2 * nVertices
    to ensure connection from any tail node to head node
    and backwards.
    :param nVertices: number of vertices of the graph.
    :return: the created graph.
    graph = GraphIL_prioritySearch()
    verticesID = []
    """
    #adding the first Vertex:
    verticesID.append((graph.addNode(None, randint(1, nVertices * 2))).id)

    #adding the remaining (n - 1) vertices:
    for i in range(nVertices - 1):
        newNodeID = (graph.addNode(None, randint(1, nVertices * 2))).id
        linkedNodeID = choice(verticesID)
        verticesID.append(newNodeID)
        graph.insertEdge(newNodeID, linkedNodeID)
        graph.insertEdge(linkedNodeID, newNodeID)
    
    return graph