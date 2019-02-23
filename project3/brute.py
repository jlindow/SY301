
#!/usr/bin/python

#################################################################################
#   Public - Private Key Brute Force                                            #                                   
#   Author: Jacob A. Lindow                                                     #                      
#                                                                               #
#   SY301 - Project 3                                                           # 
#                                                                               #
#################################################################################
#################################################################################
# Usage: $ python3 brute.py public.dot message.txt KEYSIZE MSG_HASH             #
#                                                                               #
# Functionality:                                                                #
#   1) Read public key into a graph                                             #
#   2) Return the list of all vertices (by ID name) in graph                    #
#   3) Get every combination of vertices (given keysize)                        #
#   4) Convert sum of each combination to text, hash, and compare with MSG_HASH #
#   5) Print correct msg                                                        # 
#################################################################################

import itertools
import hashlib
import sys
import random
#################################################################################
class Node: 
    def __init__ (self, name): 
        self.name           = name 
        self.value          = random.randint(1, 100)  
        self.neighborSum    = self.value  
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


        #Make the sum of all nodes equal msg 
        graphSum = 0 
        for key in self.vmap: 
            graphSum += self.vmap[key].value

            name = self.vmap[key].name
    
            self.vmap[name].value += (msg - graphSum)


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


#Read Message.txt
vertexList = []

with open(sys.argv[2], 'r') as msgFile: 
    for line in msgFile: 
            lineList = line.strip('\n').split(" ")
            vertexList.append(lineList)             

#Get list of every combination of vertices 
comboList    = list(itertools.combinations(vertexList, int(sys.argv[3])))

for i in range(len(comboList)): 
    comboSum    = 0 
    combination = comboList[i] 
    for j in range(len(combination)):
        comboSum += int(combination[j][1].rstrip()) 
    
    #Convert sum to str and hash 
    try: 
        text    = comboSum.to_bytes( (comboSum.bit_length() // 8 ) + 1, byteorder = 'big').decode('ascii').rstrip()
        myHash  = hashlib.md5(text.encode()).hexdigest()
   
        
        if myHash == sys.argv[4]: 
            print("\n\tPlaintext: " + text + "\n")
            break
            
    except:
        continue
    
