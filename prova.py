from performance import *

def disegnaGrafo(nVertices):
    g = buildGraph(nVertices)
    addEdges(g,1)
    print(g.numEdges())
    for i in g.getEdges():
        print("Da = "+str(i.head))
        print("A = "+str(i.tail))