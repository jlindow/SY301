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

    def addNeighbor(self, neighbor):
        self.adjacentList.append(neighbor)

class Graph: 

    def __str__(self):
        edgeList = [] #list of strings, e.g. "A -- B"

        string = "\ngraph " + self.name + " {\n\n\t" 
        
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices[i].adjacentList)):
                    node = self.vertices[i].adjacentList[j].name
                    edge = str(self.vertices[i].name) + " -- " + str(node)
                    oppEdge = str(node) + " -- " + str(self.vertices[i].name) 

                    if oppEdge not in edgeList: 
                        edgeList.append(edge)

        for i in range(len(edgeList)): 
            string += edgeList[i] + ";\n\t"

        string += "\n}"


        return string
    
    def __init__ (self, filename): 
        self.vertices = [] 
        self.name = "" 

        with open(filename, 'r') as graph:

            #get name
            for line in graph: 
                if line.startswith("graph"): 
                    broken = line.split(" ")
                    self.name = broken[1] 
                    #print("Graph name: " + self.name) 
            
                elif line.startswith("}"): 
                    break

                else:
                    vrtA = False
                    vrtB = False

                    broken = line.split(" -- ")
                    
                    #Get Vertex Names
                    nameA = broken[0].strip()  
                    nameB = broken[1].strip().rstrip(';')
                    
                    #determine if already in graph and set flag
                    for i in range(len(self.vertices)):
                        if self.vertices[i].name == nameA:
                            vrtA = True
                            indxA = i 
                        if self.vertices[i].name == nameB:
                            vrtB = True
                            indxB = i
                    
                    #Both in graph
                    if vrtA and vrtB == True:
                        #print("CASE 1: " +  nameA + " and " + nameB + " in graph")
                            
                        #go find both and add the other vertex to adjacent list     
                        for i in range(len(self.vertices)):
                            if self.vertices[i].name == nameA: 
                                self.vertices[i].adjacentList.append(self.vertices[indxB])
                            
                            if self.vertices[i].name == nameB:
                                self.vertices[i].adjacentList.append(self.vertices[indxA])

                    #A in graph, B not
                    elif (vrtA == True) and (vrtB == False):
                        #print("CASE 2: " + nameA + " in graph, but " + nameB + " not in graph")
                        
                        #go get index of vertexA
                        for i in range(len(self.vertices)):
                            if self.vertices[i].name == nameA:
                                savedIndexA = i 
                    
                        
                        #make a new vertex
                        vertexB = Vertex(nameB, [self.vertices[savedIndexA]]) 
                        #add new vertex to grpah
                        self.vertices.append(vertexB)
                        #link new vertex to A (already in graph)
                        self.vertices[savedIndexA].adjacentList.append(vertexB) 
    
                    
                    #B in graph, A not
                    elif (vrtB == True) and (vrtA == False): 
                        #print("CASE 3: " + nameB + " in graph, but " + nameA + "not in graph")
                        
                        #go get index of VertexB 
                        for i in range(len(self.vertices)):
                            if self.vertices[i].name == nameB:
                                savedIndexB = i 

                        #make new vertex
                        vertexA = Vertex(nameA, [self.vertices[savedIndexB]])
                        #add new vertex to graph
                        self.vertices.append(vertexA)
                        #link new vertex to B (already in graph)
                        self.vertices[savedIndexB].adjacentList.append(vertexA)
                            

                    #Neither in graph
                    else:  
                        #print("CASE 4: Neither in graph")

                        #make new vertices
                        vertexA = Vertex(nameA, [])
                        vertexB = Vertex(nameB, [vertexA]) 

                        #link vertexB to vertex A
                        vertexA.adjacentList.append(vertexB)
                        
                        #add them both to the graph
                        self.vertices.append(vertexA)
                        self.vertices.append(vertexB)

    def isAdjacent(self, vertexA, vertexB): 
       
        #iterate through graph
        for i in range(len(self.vertices)):
            
            #until vertexA is found
            if self.vertices[i].name == vertexA:
                
                #iterate through adjacent list of vertexA
                for j in range(len(self.vertices[i].adjacentList)):

                    #until vertexB is found
                    if self.vertices[i].adjacentList[j].name == vertexB:
                        return True
 
        #otherwise false 
        return False

    def returnAdjacent(self, vertex): 
        
        #iterate through graph 
        for i in range(len(self.vertices)):
            
            #until desired vertex is found
            if self.vertices[i].name == vertex:
                print("Adjacent list for vertex: " + str(self.vertices[i].name))
                nameList = []
        
                #and then return the adjacent list
                for j in range(len(self.vertices[i].adjacentList)):
                    nameList.append(self.vertices[i].adjacentList[j].name)

                return nameList



myGraph = Graph("newfile.txt")
print(myGraph.isAdjacent('A', 'B')) #TRUE
print(myGraph.isAdjacent('F', 'B')) #FALSE


print(myGraph)
