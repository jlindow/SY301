#     Directed Graph Hopper
#    Author: Jacob A. Lindow
#
#       SY301 - 9991
#    Dr. Travis Mayberry
#
#       2 Dec 2018 

class Vertex:

    def __init__(self, vertex, adjacentList):
        self.name         = vertex       #string
        self.adjacentList = adjacentList #list 

    def addNeighbor(self, neighbor):
        self.adjacentList.append(neighbor)

class Graph: 
 
    def __init__ (self, filename): 
        self.vertices = [] 
        self.name = "" 

        with open(filename, 'r') as graph:

            #get name
            for line in graph:
                DIR = False 

                if line.startswith("graph"): 
                    broken = line.split(" ")
                    self.name = broken[1] 
                    #print("Graph name: " + self.name) 
            
                elif line.startswith("}"): 
                    break

                else:
                    vrtA = False
                    vrtB = False
                    
                    if " -> " in line:
                        broken = line.split( " -> ") 
                        DIR = True
                    else: 
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
                            
                        #go find both and add the other vertex to adjacent list     
                        for i in range(len(self.vertices)):
                            if self.vertices[i].name == nameA: 
                                self.vertices[i].adjacentList.append(self.vertices[indxB])
                            
                            if DIR == False: #NON DIRECTED GRAPH
                                if self.vertices[i].name == nameB:
                                    self.vertices[i].adjacentList.append(self.vertices[indxA])

                    #A in graph, B not
                    elif (vrtA == True) and (vrtB == False):
                        
                        #go get index of vertexA
                        for i in range(len(self.vertices)):
                            if self.vertices[i].name == nameA:
                                savedIndexA = i 
                    
                        
                        #make a new vertex
                        vertexB = Vertex(nameB, []) 
                        #add new vertex to grpah
                        self.vertices.append(vertexB)

                        #link new vertex to A (already in graph)
                        self.vertices[savedIndexA].adjacentList.append(vertexB) 
                        
                        if DIR == False: 
                            vertexB.adjacentList.append(self.vertices[savedIndexA])
                    
                    #B in graph, A not
                    elif (vrtB == True) and (vrtA == False): 
                        
                        #go get index of VertexB 
                        for i in range(len(self.vertices)):
                            if self.vertices[i].name == nameB:
                                savedIndexB = i 

                        #make new vertex
                        vertexA = Vertex(nameA, [self.vertices[savedIndexB]])
                        #add new vertex to graph
                        self.vertices.append(vertexA)

                        if DIR == False: 
                            #link new vertex to B (already in graph)
                            self.vertices[savedIndexB].adjacentList.append(vertexA)
                            

                    #Neither in graph
                    else:  

                        #make new vertices
                        vertexA = Vertex(nameA, [])
                        vertexB = Vertex(nameB, []) 

                        #link vertexB to vertex A
                        vertexA.adjacentList.append(vertexB)
                        
                        if DIR == False: 
                            vertexB.adjacentList.append(vertexA)

                        #add them both to the graph
                        self.vertices.append(vertexA)
                        self.vertices.append(vertexB)

    def hopper(self, name, hops): 
        nodesInRange = set()    
        vertexList = []
        counter = 0

        #go find root vertex
        for i in range(len(self.vertices)): 
            if self.vertices[i].name == name: 
                root = self.vertices[i] 
                vertexList.append(root)
                break
 
        while (counter < hops): 
            print("counter: " + str(counter)) 
            print("Current nodes found: " + str(nodesInRange))

            vertexList = self._hopper(vertexList)
            counter += 1

            #add the stuff we just got to the list of nodes, and then go get all their neighbors
            #and make sure not already in the list

            for i in range(len(vertexList)): 
                if vertexList[i] not in nodesInRange: 
                        nodesInRange.add(vertexList[i].name) 

        #go remove the root vertex from the list
        nodesInRange.remove(root.name)
        
        return nodesInRange

    def _hopper(self, vertexList):
        myList = []
         
        #go get everything one hop further away
        for i in range(len(vertexList)): 
            vertex = vertexList[i] 
            for j in range(len(vertex.adjacentList)): 
                myList.append(vertex.adjacentList[j]) 

        return myList


myGraph = Graph(#FILENAME)
print(myGraph.hopper(#ELEMENT, #HOPS))


