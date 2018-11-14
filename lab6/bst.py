#      Binary Search Tree   
#    Author: Jacob A. Lindow
#   
#         SY301-9991
#   
#     Dr. Travis Mayberry
#        12 Nov 2018
#

class Node:
    
    def __init__(self, data): 
        self.data   = data
        self.left   = None
        self.right  = None


class TreeSet:

    def __init__(self):
        self.root   = None


    def insert(self, phrase): 

        newNode = Node(phrase)
        
        if self.root: 
            self.__insert(self.root, newNode)
        
        else: 
            self.root = newNode


    def __insert(self, currentNode, newNode):

        if (newNode.data > currentNode.data): 

            if (currentNode.right == None):   
                currentNode.right = newNode

            else: 
                self.__insert(currentNode.right, newNode)
    
        else: 
            if (currentNode.left == None): 
                currentNode.left = newNode
            
            else: 
                self.__insert(currentNode.left, newNode)  



    def __contains__(self, phrase): 
        
        if (self.__find(phrase, self.root)):
            return True
        else: 
            return False

    def __find (self, value, node): 
        
        if not node: 
            return None
        
        elif node.data == value:
            return node

        elif value < node.data: 
            return self.__find(value, node.left)

        else: 
            return self.__find(value, node.right) 

myTree = TreeSet()
myTree.insert("hello")
myTree.insert("one")
myTree.insert("two")
myTree.insert("three")
myTree.insert("four")

if "four" in myTree: 
    print("True") 
else:
    print("False")








