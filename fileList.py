#
#       Log Reader
#   Author: Jacob Lindow
#       18 Oct 18
#
#
#         SY301
#  Dr. Travis Mayberry, USNA
#

import sys

class node: 

    def __init__ (self, data):

        self.data = data
        self.nextNode = None

class linkedList: 

    def __init__ (self):
        self.head = None

    def push(self, data):
        newNode = node(data)
        
        if (self.head == None): 
            self.head = newNode

        else: 
            newNode.nextNode = self.head
            self.head = newNode

    def pop(self): 
        data = self.head.data
        nextNode = self.head.nextNode
        self.head = nextNode
        return data

    def peek(self): 
        return self.head.data

    def printReverse(self): 
        self.__printReverse(self.head) 
        return

    def __printReverse(self, node): 
        if (node == None): 
            return 
        else: 
            self.__printReverse(node.nextNode) 
            print(str(node.data), end = '') 
            print("->", end = '') 
   

################################################################################

logStack = linkedList() #create a stack

with open(sys.argv[1]) as log: #push every line of log onto stack 
    for line in log: 

        line    = line.split()
        command = line[0] 
        if (command != "exit"): #no arg for exit command
            arg    = line[1]


        if ("ssh" ==  command): 
            logStack.push(arg)

        if ('exit' == command): 
            logStack.pop()

        if ("less" == command):
            logStack.printReverse()
            print(str(arg))


