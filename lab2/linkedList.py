#
#       Lab 2
#   MIDN 2/C Lindow
#
#       SY301
# Dr. Travis Mayberry
#

class Node: 
    
    def __init__ (self, data):

        self.data       = data 
        self.nextNode   = None

class LinkedList: 

    def __init__ (self): 
        self.head = None
        self.tail = None

    def printAll (self): 
        current = self.head 

        if (current == None): #empty list
            print("\n")
            return 1
        
        while (current.nextNode != None): #breaks when current == self.tail
            print(str(current.data) + "  ")
            current = current.nextNode

        print(current.data) #print tail

        return 0 
    
    def add2Front (self, data): 
        newNode = Node(data) #initialize new node

        if (self.head == None): #check for empty list
            self.head = newNode
            self.tail = newNode 

        else:
            tmpNode = self.head #preserve current head 
            self.head = newNode #change head to newNode
            newNode.nextNode = tmpNode #reassign old head as the next node
            
        return 0 
    
    def add2Back (self, data): 
        newNode = Node(data) #initialize new node 
        
        if (self.tail == None): #check for empty list
            self.head = newNode 
            self.tail = newNode 

        else: 
            self.tail.nextNode = newNode #add newNode to back of list
            self.tail = newNode #change value of tail

        return 0 

    def isIn (self, data): 
        current = self.head #make an iterator
        tmpNode = Node(data) #store data in a node

        while (current.nextNode != None):
        
            if(current.data == tmpNode.data): 
                return True #data is in list 
        
            current = current.nextNode
        
        return False

    def addinOrder (self, data): 
        current     = self.head 
        previous    = self.head  
        tmpNode     = Node(data) #node to insert

        if (self.head.data > tmpNode.data): #tmpNode becomes head
            tmpNode.nextNode = self.head 
            self.head = tmpNode 
            return 1 

        if (self.tail.data < tmpNode.data): #tmpNode becomes tail 
            self.tail.nextNode = tmpNode 
            self.tail = tmpNode 
            return 1

        while (current.data < tmpNode.data): 
            previous = current
            current = current.nextNode 

        #loop breaks at insertion point
        tmpNode.nextNode = current
        previous.nextNode = tmpNode

        return 0
    
