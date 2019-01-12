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


        def isEmpty(self):
            """
            method used to understand if the 
            graph is empty or not.
            :return: boolean.
            """
            return self.nodes == {}

        def isFull(self):
            """
            method used to understand if the 
            graph is full or not.
            :return: boolean.
            """            
            maxCapacity = self.numNodes() * (self.numNodes() - 1)
            return self.numEdges() == maxCapacity

        def prioritySearch_PQbinaryHeap(self):
            """
            This algorithm executes a prioritySearch 
            based on the genericSearch of a graph. 
            It uses a list to represent the visit of the graph and
             a Binary Heap as priority queue for the nodes to explore.
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
            This algorithm executes a prioritySearch
            based on the genericSearch of a graph. 
            It uses a list to represent the visit of the graph and 
            a Binomial Heap as priority queue for the nodes to explore.
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
            This algorithm executes a prioritySearch 
            based on the genericSearch of a graph. 
            It uses a list to represent the visit of the graph and
            a D-Heap as priority queue for the nodes to explore.
            :param d: size of the d-heap.
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
    Build a Graph ready for prioritySearch()
    using random weights and random edges 
    between vertices.
    The graph will have as may edges as (2 * nVertices - 2 ) 
    (the first vertex added is not going to be linked)
    to ensure connection from any tail node to head node
    and backwards.
    :param nVertices: number of vertices of the graph.
    :return: the created graph.
    """
    graph = GraphIL_prioritySearch()
    verticesID = []
    
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


def addVertices(graph, nVertices):
    """
    Add as many nodes as param nVertices,
    mantaining the convention of using weights in range
    (1 to 2 * number of final vertices).
    The function modifies the graph in place. ( no return value needed )
    :param graph: graph to modify.
    :param nVertices: number of vertices to add.
    """
    if graph.isEmpty():
        verticesID = []
        verticesID.append((graph.addNode(None, randint(1, nVertices * 2))).id)
        
        for i in range(nVertices - 1):
            newNodeID = (graph.addNode(None, randint(1, nVertices * 2))).id
            linkedNodeID = choice(verticesID)
            verticesID.append(newNodeID)
            graph.insertEdge(newNodeID, linkedNodeID)
            graph.insertEdge(linkedNodeID, newNodeID)

    else:
        #retrieving previous id:
        verticesID = list(graph.nodes.keys())
        weightRange = (len(verticesID) + nVertices) * 2
        for i in range(nVertices):
            newNodeID = (graph.addNode(None, randint(1, weightRange))).id
            linkedNodeID = choice(verticesID)
            verticesID.append(newNodeID)
            graph.insertEdge(newNodeID, linkedNodeID)
            graph.insertEdge(linkedNodeID, newNodeID)



def addEdges(graph, nEdges):
    """
    Add as many edgs as param nEdges, 
    avoiding to add edges from a vertex to itself.
    The function modifies the graph in place. ( no return value needed )
    :param graph: graph to modify.
    :param nEdges: number of edges to add.
    """
    assert (not graph.isEmpty()), "graph must contain at least an element."
    assert (not graph.isFull()), "graph is already full."
    assert (graph.numEdges() + 2 * nEdges <= graph.numNodes() * graph.numNodes() - 1), "too many edges to add."
    verticesID = list(graph.nodes.keys())
    for i in range (nEdges):
        headVertex = choice(list(filter(lambda i: sorted(graph.getAdj(i) + [i]) != sorted(verticesID), verticesID)))

        tailVertex = choice(list(filter(lambda i : i not in graph.getAdj(headVertex)+[headVertex], verticesID)))
        
        graph.insertEdge(headVertex, tailVertex)
        graph.insertEdge(tailVertex, headVertex)