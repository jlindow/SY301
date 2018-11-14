#        Lab 6, Part 3
#   Author: Jacob A. Lindow
#   
#          SY301-9991
#      Dr. Travis Mayberry
#

########## import classes ##############
import sys

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
        
        elif value == node.data:
            return node

        elif value < node.data:
            return self.__find(value, node.left)

        else:
            return self.__find(value, node.right) 
####### fill tree with bad words #######

wordTree = TreeSet() 

with open("badWords.txt", "r") as badWords: 
   
    while True: 
        word = badWords.readline() 
        if (word == ""): 
            break 
        wordTree.insert(word.strip()) 

####### search tree for words ###########

with open(sys.argv[1], "r") as text: 
    wordList = []
    for line in text: 
        for word in line.split(): 
            wordList.append(word.lower().strip())

count = 0
for i in range(len(wordList)):

    phrase = wordList[i] 

    for j in range(5):
        x = (i + j)

        if ( x >= len(wordList)):
            x = (len(wordList) - 1) 
        
        if (j != 0): 
            phrase = str(phrase.strip() + " " + wordList[x].strip()) 
         
        if phrase.strip() in wordTree: 
            print(phrase)
            count += 1
            break

print("Count: " + str(count)) 

