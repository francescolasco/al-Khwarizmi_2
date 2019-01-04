from PQ_Dheap import PQ_DHeap
from PQbinaryHeap import PQbinaryHeap
from PQbinomialHeap import PQbinomialHeap
from graph.Graph import *

def prioritySearch_PQbinaryHeap(graph):
	"""
	This algorithm executes a prioritySearch based on the genericSearch of a graph. 
	It uses a list to represent the visit of the graph and a priority queue for the nodes to explore.
	:param graph: a graph to explore.
	:return: the list of the exploration.
	"""
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
		
		for vertex in graph.getAdj(u):
			ID = vertex.id
			KEY = -(vertex.key)
			if ID not in exploredNodes:
				pq.insert(ID, KEY)

	return exploredNodes
