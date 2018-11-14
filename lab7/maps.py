#           Lab 7 
#   Author: Jacob A. Lindow
#
#         SY301-9991
#     Dr. Travis Mayberry
#
#         14 Nov 18
#

import bisect

class KVPair: 
    
    def __init__(self, key, value):
        self.key = key
        self.value = value

    #LESS THAN
    def __lt__(self, other): 
        if self.key < other.key:
            return True
        else:
            return False

    #GREATER THAN
    def __gt__(self, other): 
        if self.key > other.key:
            return True
        else:
            return False

    #LESS THAN OR EQUAL
    def __le__(self, other): 
        if self.key <= other.key: 
            return True
        else:
            return False

    #GREATER THAN OR EQUAL
    def __ge__(self, other): 
        if self.key >= other.key:
            return True
        else:
            return False
    #EQUAL
    def __eq__(self, other): 
        if self.key == other.key:
            return True
        else:
            return False

    #NOT EQUAL    
    def __ne__(self, other): 
        if self.key != other.key:
            return True
        else:
            return False

class SortedArrayMap:

    def __init__(self):
        self.arrayMap = []

    def __setitem__(self, k, v): 
        
        pair = KVPair(k,v)
        bisect.insort_left(self.arrayMap, pair)
    
    def __getitem__(self, k): 
        
        for i in range(len(self.arrayMap)): 
            if (self.arrayMap[i].key == k): 
                return self.arrayMap[i].value

    def __contains__(self, k): 

        for i in range(len(self.arrayMap)):
            if (self.arrayMap[i].key == k): 
                return True

    def printAll(self):
        for i in range(len(self.arrayMap)):
            print(str(self.arrayMap[i].key) + ", " + str(self.arrayMap[i].value))

pair1 = KVPair(160000, "Aardvark, Aaaron")
pair2 = KVPair(169999, "Zebra, Zeke")


                            #EXPECTED OUTPUT    
print(pair1<pair2)              #True   
print(pair2<pair1)              #False
print(pair2==pair1)             #False
print(pair1!=pair2)             #True


arrMap = SortedArrayMap()
arrMap[160000] = "apple"
arrMap[123] = "banana"
arrMap[2] = "pear"
arrMap[9999999] = "big fruit" 
print(arrMap[160000])           #"apple"
print(160000 in arrMap)         #True
print(169999 in arrMap)         #False
arrMap.printAll()               #2, pear
                                #123, banana
                                #160000, apple
                                #9999999, big fruit



            











