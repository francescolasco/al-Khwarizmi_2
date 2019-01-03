def prioritySearch(graph, pqType):
	"""
	This algorithm executes a prioritySearch based on the genericSearch of a graph. 
	It uses a list to represent the visit of the graph and a priority queue for the nodes to explore.
	:param graph: a graph to explore.
	:return: the list of the exploration.
	"""
	if pqType == 'PQbinary':
        pq = PQbinaryHeap()
        print("Using", pqType)
    elif pqType == 'PQbinomial':
        pq = PQbinomialHeap()
        print("Using", pqType)
    elif pqType == 'PQ_Dheap' and d is not None:  #'d' must be set.
        pq = PQ_DHeap(d)
        print("Using ", pqType, "with d = ", d)
    else:
        return
        
	exploredNodes = []

	while not pq.isEmpty():
