#!/usr/bin/python

#################################################################################
#   Public - Private Key Encryption                                             #                                   
#   Author: Jacob A. Lindow                                                     #                      
#                                                                               #
#   SY301 - Project 3                                                           # 
#                                                                               #
#################################################################################
#################################################################################
# Usage: $ python3 enc.py public.dot msg.txt                                    #
#                                                                               #
# Functionality:                                                                #
#   1) Read msg.txt and convert to an integer                                   #
#   2) Create a new graph with nodes public.dot                                 #
#       - While creating graph, assign random number values to each node        #
#   3) Make the last node some int such that the sum equals the msg integer     #
#   4) Iterate through the graph and assign a second num to each node           #
#      equal to the sum of all neighbors first num                              #
#   5) Create a cipherText with every nodeName and corresponding second int     #
#       e.g      nodeName + " " + INT + "\n" + nodeName etc...                  #
#   6) Output cipherText                                                        #
#################################################################################
import sys
import random
################################################################################# 
class Node: 
    def __init__ (self, name): 
        self.name           = name 
        self.value          = random.randint(1, 100)  
        self.neighborSum    = 0 
        self.neighbors      = set() 
    
    def addNeighbor(self, neighbor): 
        self.neighbors.add(neighbor)

    def __str__ (self): 
        return str(self.name) 

class Graph:
    def __init__ (self, fname):
        """ Read in dot file and create a graph """ 
        with open(fname) as dotin: 
            wholefile = dotin.read() 

        openbrace   = wholefile.index('{') 
        closebrace  = wholefile.index('}')
        
        gtype, self._gname = wholefile[:openbrace].split()
        edgesep = '--'

        self.vmap = {}

        for edgestr in wholefile[openbrace+1:closebrace].split(';'): 
            left, sep, right = edgestr.partition(edgesep)
            if sep == "": 
                continue 

            a = left.strip() 
            b = right.strip() 

            if a not in self.vmap: 
                self.vmap[a] = Node(a) 
            if b not in self.vmap: 
                self.vmap[b] = Node(b) 

            self.vmap[a].addNeighbor(self.vmap[b])
            self.vmap[b].addNeighbor(self.vmap[a]) 

    def isAdjacent(self, vertexA, vertexB): 
        return self.vmap[vertexB] in self.vmap[vertexA].neighbors 

    def neighbors(self, vertexA): 
        return list(self.vmap[vertexA].neighbors) 

    def vertices(self): 
        return list(self.vmap) 

    def encode(self, msg): 
        msg = int.from_bytes(str.encode(msg, 'ascii'), byteorder = 'big') 
        print("Message: " + str(msg)) 

        #Make the sum of all nodes equal msg 
        graphSum = 0 
        for key in self.vmap: 
            graphSum += self.vmap[key].value
            
            name = self.vmap[key].name
    
        self.vmap[name].value += (msg - graphSum)

        print("Graph Sum: " + str(graphSum))
       
        for key in self.vmap: 
            print("KEY: " + self.vmap[key].name + ", VALUE: " + str(self.vmap[key].value)) 
        
        #Make the second int for each node the sum of all neighbors
        for key in self.vmap:
            secondInt = 0; 

            neighborList   = self.neighbors(self.vmap[key].name) 
    
            for i in range(len(neighborList)):
                secondInt += neighborList[i].value       
            
            secondInt += self.vmap[key].value 
            self.vmap[key].neighborSum = secondInt 
        
        #Create ciphertext
        ciphertext = "" 
        for key in self.vmap: 
            ciphertext += str(self.vmap[key].name) + " " + str(self.vmap[key].neighborSum) + "\n"
        return ciphertext    


#################################################################################

#Read msg.txt and convert to an integer 
with open(sys.argv[2]) as msgFile: 
    msg = msgFile.read() 
    
#Create a graph with nodes from public key
publicKey   = Graph(sys.argv[1]) 
ciphertext  = publicKey.encode(msg)
print(ciphertext)


