class Node:
  def __init__(self, data):
    self.data = data
    self.nextNode = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

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

  def printInOrder(self):
      self._printInOrder(self.head)
      return 0

  def __printInOrder(self, node):

      if(node == self.tail):
          print(str(node.data) + " ")
          return 0
      else:
          print(str(node.data) + " ")
          nextNode = node.nextNode
          self._printInOrder(nextNode)

  def printInReverseOrder(self):



  def isIn(self, element):



  def isInTimes(self, element):
    '''Returns an integer, which is the number of times element appears in
    the list'''
    pass

  def get(self, i):
    '''Returns the data at index i (counting from 0).  You may assume i is a
    valid index'''
    pass

  def addBefore(self, findElement, addElement):
    '''Adds addElement to the list, so that it appears right before the first
    appearance of findElement in the list.  If findElement is not in the list,
    addElement should be added to the end of the list.'''
    pass

  def remove(self, i):
    '''Alters the linked list such that the i-th element is removed.  You may
    assume i is a valid index.'''
    pass
