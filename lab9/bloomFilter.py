#         Bloom Filter
#   Author: Jacob A. Lindow
#   
#           SY301
#     Dr. Travis Mayberry
#       27 November 18
#

import hashlib

class bloom:

    def __init__(self, size): 
        self.list = [False] * size
        return

    def add(self, k): 

        for i in range(1,3): 
            hashOut = self.hashFunc(i, k)
            index = hashOut % len(self.list)
            self.list[index] = True

    def __contains__(self, k):
    
        for i in range(1, 3): 
            hashOut = self.hashFunc(i, k)
            index = hashOut % len(self.list)
            if (self.list[index] == False):
                return False #(definitely false)

        return True #(sorta... probably true)

    def hashFunc(self, hashType, inputVal): 
        if (hashType == 1): 
                hashObject = hashlib.md5()
        if (hashType == 2): 
                hashObject = hashlib.sha256()
        if (hashType == 3): 
                hashObject = hashlib.sha512()

        byteString = inputVal.encode()
        hashObject.update(byteString)
        hexString = hashObject.hexdigest()

        output = int(hexString, 16)

        return output
 
bloomFil = bloom(524288)
bloomFil.add("hello")
bloomFil.add("jake")
bloomFil.add("carissa")

if "carissa" in bloomFil:
    print("Carissa in set") 

if "jake" in bloomFil: 
    print("Jake also in set")

if "hello" in bloomFil: 
    print("3 for 3")

if "pumpkin" not in bloomFil: 
    print("No pumpkin for you")

