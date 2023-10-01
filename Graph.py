class Graph:
    def __init__(self):
        self.adjacencyList = {}
    
    def addVertex(self,vertex):
        if vertex not in self.adjacencyList.keys():
            self.adjacencyList[vertex] = []
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adjacencyList:
            print(vertex,':',self.adjacencyList[vertex])

    