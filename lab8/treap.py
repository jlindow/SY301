#           Lab 8 
#   Author: Jacob Lindow
#
#       SY301 - 9991
#     Dr. Travis Mayberry
#
#        14 Nov 18
#
# sources used: https://stackoverflow.com/questions/15214852/depth-of-a-tree-python
#               http://opendatastructures.org/ods-python/7_2_Treap_Randomized_Binary.html
#               http://www.grantjenks.com/wiki/random/python_treap_implementation
#               https://www.geeksforgeeks.org/treap-set-2-implementation-of-search-insert-and-delete/

import random

class treapNode: 

    def __init__(self, data): 
        self.priority   = random.uniform(0, 1)
        self.data       = data
        self.left       = None
        self.right      = None
        self.parent     = None

    def depth(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return self.right.depth() + 1
        elif self.right == None:
            return self.left.depth() + 1
        else:
            return max(self.left.depth(), self.right.depth()) + 1

class TreapSet:

    def __init__(self):
        self.root = None
        self.length = 0

    def add(self, k): 
        newNode = treapNode(k)

        if self.root: 
            self.__add(self.root, newNode)
        else:
            self.root = newNode
    
        self.organize(newNode)

        self.length += 1

    def __add(self, currentNode, newNode):

        if (newNode.data > currentNode.data): 

            if (currentNode.right == None):   
                currentNode.right = newNode
                newNode.parent = currentNode

            else: 
                self.__add(currentNode.right, newNode)
    
        else: 
            if (currentNode.left == None): 
                currentNode.left = newNode
                newNode.parent = currentNode
            
            else: 
                self.__add(currentNode.left, newNode)

    def organize(self, node):
        #rotate until the priority of the current node is greatest
        while (node.parent and node.parent.priority) < node.priority:
            self.rotate(node)
    
    def rotate(self, node):
        
        #get parent of current node
        parent = node.parent
        if parent == None: 
            return
    
        #clockwise rotation
        #if current node is to left of the parent
        if parent.left == node: 
            #shift parent node down to the right of current node
            node.right = parent 
            #shift current node's kids to under parent
            parent.left = node.right

            #from line 89, if parent.left exists, make sure it knows who its parents are
            if parent.left: 
                parent.left.parent = parent

        #counter-clockwise rotation
        #current node is to the right of parent 
        #same as above, just opposite
        else:
            node.left = parent
            parent.right = node.left

            if parent.right:
                parent.right.parent = parent

        #reassign parents for nodes that moved       
        grandparent = parent.parent
        node.parent = grandparent 
        parent.parent = node

        #rotated node is NOT a child of root node.
        if grandparent != None:
            #if we did a clockwise rotation
            if grandparent.right == parent:
                grandparent.right = node
            #if we did a counter clockwise rotation
            else:
                grandparent.left = node
        else:
            #means we rotated a child of the root node, so it is now the new root
            self.root = node

    def __contains__(self, k): 
        
        if (self.__find(k, self.root)):
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
        

    def __len__(self): 
        return self.length    
    
    def height(self):
        return self.root.depth()
    

