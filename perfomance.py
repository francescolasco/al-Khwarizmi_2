from Graph_IncidenceList_MOD import *
from random import randint

def generateWeightedGraph(numNodes):
	graph = GraphIncidenceList()

	graph.print()

	for i in range(numNodes):
		graph.addNode(i, randint(1, numNodes))

	graph.print()