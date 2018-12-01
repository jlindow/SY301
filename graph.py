#
#
#
#
#
#
#
#


class Vertex:

    def __init__(self, vertex, adjacentList):
        self.name         = vertex       #string
        self.adjacentList = adjacentList #list 

    def addNeighbor(self, vertex, neighbor):
        vertex.adjacentList.append(neighbor)

class Graph: 

    def __init__ (self, filename): 
        self.vertices = [] 
        self.name = "" 

        with open(filename, 'r') as graph:
           
            #get name
            for line in graph: 
                if line.startswith("graph"): 
                    broken = line.split(" ")
                    self.name = broken[1] 
                    print("Graph name: " + self.name) 
            
                elif line.startswith("}"): 
                    break

                else:
                    broken = line.split(" -- ")
                        
                    #Get Vertices
                    vertexA = broken[0].strip()  
                    vertexB = broken[1].strip().rstrip(';')
                    print("VertexA: " + "'" +vertexA + "'" + " VertexB: " + "'" + vertexB + "'") 


                    #Both in graph
                    if vertexA and vertexB in self.vertices:                         
                        vertexA.adjacentList.append(vertexB)
                        vertexB.adjacentList.append(vertexA)

                    #A in graph, B not
                    elif (vertexA in self.vertices) and (vertexB not in self.vertices):
                        vertexB = Vertex(vertexB, [vertexA]) 
                        vertexA.adjacentList.append(vertexB)
                    
                    #B in graph, A not
                    elif (vertexB in self.vertices) and (vertexA not in self.vertices): 
                        vertexA = Vertex(vertexA, [vertexB])
                        vertexB.adjacentList.append(vertexA)

                    #Neither in graph
                    else:  
                        vertexA = Vertex(vertexA, [vertexB])
                        vertexB = Vertex(vertexB, [vertexA]) 

    def isAdjacent(self, vertexA, vertexB): 
        for i in range(len(self.vertices)):
            #check for name of vertex, then if A or B in adjacent list
            if self.vertices[i].name == vertexA:
                if vertexB in self.vertices[i].adjacentList:
                    return True
        

    def returnAdjacent(self, vertex): 
        for i in range(len(self.vertices)):
            if self.vertices[i].name == vertex:
                return self.vertices[i].adjacentList




myGraph = Graph("newfile.txt")
print(myGraph.isAdjacent('A', 'B'))
print(myGraph.isAdjacent('F', 'B'))
print(myGraph.returnAdjacent('A'))

