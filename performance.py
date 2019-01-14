from Graph_IncidenceList_prioritySearch import *
from Graph_IncidenceList_prioritySearch import buildGraph
from time import *


def performanceGraphIL(graph, version, d = None):
    assert d != None, "You must provide a 'd' for the D-Heap test!"
    binaryHeapVertices = open("performanceData/performancebinaryHeapVertices.txt", "a")
    binaryHeapEdges = open("performanceData/performancebinaryHeapEdges.txt", "a")
    binomialHeapVertices = open("performanceData/performancebinomialHeapVertices.txt", "a")
    binomialHeapEdges = open("performanceData/performancebinomialHeapEdges.txt", "a")
    dHeapVertices = open("performanceData/performancedHeapVertices.txt", "a")
    dHeapEdges = open("performanceData/performancedHeapEdges.txt", "a")

    nVertices = len(graph.getNodes())
    nEdges = graph.numEdges()

    start = time()
    graph.prioritySearch_PQbinaryHeap()
    tempo = time()-start
    if version == 0:
        binaryHeapVertices.write("{}\t{}\n".format(nVertices, tempo))
    elif version == 1:
        binaryHeapEdges.write("{}\t{}\n".format(nEdges, tempo))


    start = time()
    graph.prioritySearch_PQbinomialHeap()
    tempo = time()-start
    if version == 0:
        binomialHeapVertices.write("{}\t{}\n".format(nVertices, tempo))
    elif version == 1:
        binomialHeapEdges.write("{}\t{}\n".format(nEdges, tempo))


    start = time()
    graph.prioritySearch_PQ_DHeap(d)
    tempo = time()-start
    if version == 0:
        dHeapVertices.write("{}\t{}\n".format(nVertices, tempo))
    elif version == 1:
        dHeapEdges.write("{}\t{}\n".format(nEdges, tempo))

    binaryHeapVertices.close()
    binaryHeapEdges.close()
    binomialHeapVertices.close()
    binomialHeapEdges.close()
    dHeapVertices.close()
    dHeapEdges.close()




def dataVertices(maxV, d):
    for vertices in range(10,maxV+1,10):
        graph = buildGraph(vertices)
        performanceGraphIL(graph, 0, d)


def dataEdges(nVertices, d):
    graph = buildGraph(nVertices)
    nEdges = graph.numEdges()
    maxEdges = int((nVertices*(nVertices-1)))-nEdges
    print("maxE = "+str(maxEdges))
    for edges in range(100):
        performanceGraphIL(graph, 1, d)
        addEdges(graph, int(maxEdges/100))


def dataForGraphs(nVertices, maxV, d):
    dataVertices(maxV, d)
    dataEdges(nVertices, d)


def ereaseDataFromGraphs():
    binaryHeapVertices = open("performanceData/performancebinaryHeapVertices.txt", "w+").close()
    binaryHeapEdges = open("performanceData/performancebinaryHeapEdges.txt", "w+").close()
    binomialHeapVertices = open("performanceData/performancebinomialHeapVertices.txt", "w+").close()
    binomialHeapEdges = open("performanceData/performancebinomialHeapEdges.txt", "w+").close()
    dHeapVertices = open("performanceData/performancedHeapVertices.txt", "w+").close()
    dHeapEdges = open("performanceData/performancedHeapEdges.txt", "w+").close()