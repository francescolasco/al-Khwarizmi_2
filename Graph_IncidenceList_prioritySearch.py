from priorityQueue.PQ_Dheap import PQ_DHeap
from priorityQueue.PQbinaryHeap import PQbinaryHeap
from priorityQueue.PQbinomialHeap import PQbinomialHeap
from Graph_IncidenceList_MOD import GraphIncidenceList
from graph.Graph import *

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
                
                for vertex in self.getAdj(u):
                    ID = vertex.id
                    KEY = -(vertex.key)
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
                
                for vertex in self.getAdj(u):
                    ID = vertex.id
                    KEY = -(vertex.key)
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
            pq = PQ_DHeap()
            exploredNodes = []

            s = self.maxWeight()
            ID = s[0]
            KEY = -(s[1])
            pq.insert(ID, KEY)

            while not pq.isEmpty():
                u = pq.findMin()
                pq.deleteMin()

                exploredNodes.append(u)
                
                for vertex in self.getAdj(u):
                    ID = vertex.id
                    KEY = -(vertex.key)
                    if ID not in exploredNodes:
                        pq.insert(ID, KEY)

            return exploredNodes