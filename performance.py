from Graph_IncidenceList_prioritySearch import *
from Graph_IncidenceList_prioritySearch import buildGraph
from random import *
from timer import timer
from time import *


################################ V1 ###################################
def performanceStrana(nVertices, d = None):
    assert d != None, "You must provide a 'd' for the D-Heap test!"
    graph = buildGraph(nVertices)

    @timer
    def testPrioritySearch_PQbinaryHeap():
        graph.prioritySearch_PQbinaryHeap()

    @timer
    def testPrioritySearch_PQbinomialHeap():
        graph.prioritySearch_PQbinomialHeap()

    @timer
    def testPrioritySearch_PQ_DHeap(d):
        graph.prioritySearch_PQ_DHeap(d)

    testPrioritySearch_PQbinaryHeap()
    testPrioritySearch_PQbinomialHeap()
    testPrioritySearch_PQ_DHeap(d)

################################# V2 ##################################



def performanceGraphIL(nVertices, d = None):
    assert d != None, "You must provide a 'd' for the D-Heap test!"
    binaryHeap = open("performanceData/performancebinaryHeap.txt", "a")
    binomialHeap = open("performanceData/performancebinomialHeap.txt", "a")
    dHeap = open("performanceData/performancedHeap.txt", "a")
    graph = buildGraph(nVertices)

    start = time()
    graph.prioritySearch_PQbinaryHeap()
    tempo = time()-start
    binaryHeap.write("{}\t{}\n".format(nVertices, tempo))


    start = time()
    graph.prioritySearch_PQbinomialHeap()
    tempo = time()-start
    binomialHeap.write("{}\t{}\n".format(nVertices, tempo))


    start = time()
    graph.prioritySearch_PQ_DHeap(d)
    tempo = time()-start
    dHeap.write("{}\t{}\n".format(nVertices, tempo))

    binaryHeap.close()
    binomialHeap.close()
    dHeap.close()


numberOfVertices = [10, 100, 1000, 5000, 10000]
def dataForGraphs(nVertices, d):
    for i in numberOfVertices:
        performanceGraphIL(i, d)

def ereaseDataFromGraphs():
    binaryHeap = open("performanceData/performancebinaryHeap.txt", "w+").close()
    binomialHeap = open("performanceData/performancebinomialHeap.txt", "w+").close()
    dHeap = open("performanceData/performancedHeap.txt", "w+").close()
