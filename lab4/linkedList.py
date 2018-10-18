class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class linkedList:

    ############################################################################     

    def __init__(self):
        self.head = None
        self.tail = None

    ############################################################################    

    def add2Front(self, data):

        newNode = Node(data) #initialize new node
        if (self.head == None): #check for empty list
            self.head = newNode
            self.tail = newNode
        else:
            tmpNode = self.head #preserve current head
            self.head = newNode #change head to newNode
            newNode.nextNode = tmpNode #reassign old head as the next node

        return 0 

    ############################################################################

    def printInOrder(self):
        self.__printInOrder(self.head)
        return 0

    def __printInOrder(self, node):

        if(node == self.tail):
            print(str(node.data) + " ")
            return
        else:
            print(str(node.data) + " ")
            nextNode = node.nextNode
            self.__printInOrder(nextNode)

    ###########################################################################

    def printInReverseOrder(self):

        self.__printInReverseOrder(self.head)
        return 0

    def __printInReverseOrder(self, node): 

        if (node == None): 
            return
        else: 
            self.__printInReverseOrder(node.nextNode)
            print(str(node.data) + " ")    

    ###########################################################################

    def isIn(self, element):

        return self.__isIn(element, self.head)

    def __isIn(self, element, node):

        if (node.data == element): 
            return True

        if (node.nextNode == None): 
            return False

        return self.__isIn(element, node.nextNode) 

    ############################################################################

    def isInTimes(self, element):

        amount = self.__isInTimes(element, self.head, 0)
        return amount    

    def __isInTimes(self, element, node, count):  

        if (node.data == element): 
            count += 1

        if (node.nextNode == None): 
            return count 

        return self.__isInTimes(element, node.nextNode, count)


    ############################################################################


    def get(self, i):

        return self.__get(i, self.head, 0)

    def __get(self, i, node, currentIndex): 

        if (i == currentIndex): 
            return node.data

        currentIndex += 1
        return self.__get(i, node.nextNode, currentIndex)

    ############################################################################

    def addBefore(self, findElement, addElement):

        self.__addBefore(findElement, addElement, self.head)
        return 0


    def __addBefore(self, findElement, addElement, node): 

        if (node.nextNode == None): #at the tail 
            newNode             = Node(addElement) #make a newNode
            node.nextNode       = newNode          #link tail to newNode
            self.tail           = newNode          #assign as tail
            return

        if (node.nextNode.data == findElement):    #insert node
            newNode             = Node(addElement) #make a newnode
            newNode.nextNode    = node.nextNode    #assign the next node
            node.nextNode       = newNode          #link previous to new
            return 
        
        self.__addBefore(findElement, addElement, node.nextNode) 

    ############################################################################

    def remove(self, i):

        self.__remove(i, self.head, None, 0)

    def __remove(self, i, node, prev, currentIndex): 

        if (i == 0): #remove head
            self.head = node.nextNode 
            return

        if (i == currentIndex): 
            prev.nextNode = node.nextNode
            return

        currentIndex += 1

        prev = node
        node = node.nextNode

        self.__remove(i, node, prev, currentIndex)

    ############################################################################
    # Test Code #

myLL = linkedList()
myLL.add2Front(1)
myLL.add2Front(2)
myLL.add2Front(4)
myLL.printInOrder()
myLL.printInReverseOrder()
print("\n")
myLL.addBefore(2, 3)
myLL.printInOrder()

print(myLL.isIn(3))
print(myLL.isIn(1))
print(myLL.isIn(5))
myLL.addBefore(7, 0)
myLL.add2Front(4)
print(myLL.isInTimes(4))
print(myLL.isInTimes(0))
print("List: \n") 
myLL.printInOrder()
print("\n") 
myLL.remove(0)
myLL.remove(3)
myLL.printInOrder()
print("\n") 
print(myLL.get(0))
print(myLL.get(2))

