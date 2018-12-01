#         Sorting Lab
#   Author: Jacob A. Lindow
#
#       SY301 - 9991
#     Dr. Travis Mayberry
#       
#         1 Dec 2018

class PCAP: 
    
    def __init__(self, filename): 
        self.file = filename
        self.entries = []
        
        #open file, create a log entry for each line
        with open(filename, 'r') as log: 
            for line in log: 
                if (line != "\n"):
                    newEntry = entry(line) 
                    self.entries.append(newEntry)
    
    def ipsByConnections(self): 
        tupList = []
        
        #iterate through all entries, O(n)
        for i in range(len(self.entries)): 
            
            #get a source 
            source = self.entries[i].source
            
            #check if source in tupList
            added = False
            for j in range(len(tupList)): 
                
                #source in tupList, so get current value
                if tupList[j][0] == source:
                    currentValue = tupList[j][1]
                    newValue = int(currentValue) + 1
                        
                    #make new tuple
                    newTup = (source, int(newValue)) 
                    #reassign
                    tupList[j] = newTup
                    
                    #sources won't appear in tupList multiple times, so break
                    added = True
                    break

            if added == False: 
                #source NOT in tuplist, so only make a new tuple
                newTup = (source, int(1)) 
                #add to tupList
                tupList.append(newTup) 


        #SORT TUPLIST O(log(n))
        sortedList = str(mySort(tupList, 1)) 
    
        #return sorted tuple list
        return sortedList


    def ipsByBytes(self):
        tupList = []
        
        #iterate through all entries, O(n)
        for i in range(len(self.entries)): 
            
            #get a source 
            source = self.entries[i].source
            size   = self.entries[i].bytes

            #check if source in tupList
            added = False
            for j in range(len(tupList)): 
                
                #source in tupList, so get current value 
                if tupList[j][0] == source: 

                    currentValue = tupList[j][1]
                    newValue = int(currentValue) + int(size)

                    #make new tuple
                    newTup = (source, int(newValue))
                    tupList[j] = newTup

                    #sources won't appear in tupList multiple times, so break
                    added = True
                    break

            if added == False: 
                #source NOT in tuplist, so make a new tuple
                newTup = (source, int(size)) 
                #add to tupList
                tupList.append(newTup) 


        #SORT TUPLIST O(log(n))
        sortedList = str(mySort(tupList, 1)) 

        #return sorted tuple list
        return sortedList


    def protocolsByConnections(self):
        
        tupList = []
        
        #iterate through all entries, O(n)
        for i in range(len(self.entries)): 
            
            #get a source 
            protocol = self.entries[i].protocol

            #check if source in tupList
            added = False
            for j in range(len(tupList)): 
                
                #source in tupList, so get current value 
                if tupList[j][0] == protocol: 

                    currentValue = tupList[j][1]
                    newValue = int(currentValue) + 1

                    #make new tuple
                    newTup = (protocol, int(newValue))
                    tupList[j] = newTup

                    #sources won't appear in tupList multiple times, so break
                    added = True
                    break

            if added == False: 
                #source NOT in tuplist, so make a new tuple
                newTup = (protocol, 1) 
                #add to tupList
                tupList.append(newTup) 


        #SORT TUPLIST O(log(n))
        sortedList = str(mySort(tupList, 1)) 

        #return sorted tuple list
        return sortedList


    def protocolsByBytes(self): 

        tupList = []
        
        #iterate through all entries, O(n)
        for i in range(len(self.entries)): 
            
            #get a source 
            protocol = self.entries[i].protocol
            size     = self.entries[i].bytes

            #check if source in tupList
            added = False
            for j in range(len(tupList)): 
                
                #source in tupList, so get current value 
                if tupList[j][0] == protocol: 

                    currentValue = tupList[j][1]
                    newValue = int(currentValue) + int(size)

                    #make new tuple
                    newTup = (protocol, int(newValue))
                    tupList[j] = newTup

                    #sources won't appear in tupList multiple times, so break
                    added = True
                    break

            if added == False: 
                #source NOT in tuplist, so make a new tuple
                newTup = (protocol, int(size)) 
                #add to tupList
                tupList.append(newTup) 


        #SORT TUPLIST O(log(n))
        sortedList = str(mySort(tupList, 1)) 

        #return sorted tuple list
        return sortedList



    def connectionsByConnections(self):
        tupList = []
        
        #iterate through all entries, O(n)
        for i in range(len(self.entries)): 
            
            #get a source 
            source      = self.entries[i].source
            destination = self.entries[i].destination

            #check if source in tupList
            added = False
            for j in range(len(tupList)): 
                
                #connection in tupList, so get current value 
                if (tupList[j][0] == source) and (tupList[j][1] == destination): 

                    currentValue = tupList[j][2]
                    newValue = int(currentValue) + int(1)

                    #make new tuple
                    newTup = (source, destination, int(newValue))
                    tupList[j] = newTup

                    #sources won't appear in tupList multiple times, so break
                    added = True
                    break

            if added == False: 
                #source NOT in tuplist, so make a new tuple
                newTup = (source, destination, int(1)) 
                #add to tupList
                tupList.append(newTup) 


        #SORT TUPLIST O(log(n))
        sortedList = str(mySort(tupList, 2)) 

        #return sorted tuple list
        return sortedList
        



    def connectionsByBytes(self):

        tupList = []
        
        #iterate through all entries, O(n)
        for i in range(len(self.entries)): 
            
            #get a source 
            source      = self.entries[i].source
            destination = self.entries[i].destination
            size        = self.entries[i].bytes

            #check if source in tupList
            added = False
            for j in range(len(tupList)): 
                
                #connection in tupList, so get current value 
                if (tupList[j][0] == source) and (tupList[j][1] == destination): 

                    currentValue = tupList[j][2]
                    newValue = int(currentValue) + int(size)

                    #make new tuple
                    newTup = (source, destination, int(newValue))
                    tupList[j] = newTup

                    #sources won't appear in tupList multiple times, so break
                    added = True
                    break

            if added == False: 
                #source NOT in tuplist, so make a new tuple
                newTup = (source, destination, int(size)) 
                #add to tupList
                tupList.append(newTup) 


        #SORT TUPLIST O(log(n))
        sortedList = str(mySort(tupList, 2)) 

        #return sorted tuple list
        return sortedList


#each instance of this  class represents one entry in the logfile
class entry:

    #string represents one line from the csv file
    def __init__(self, string):
        
        #split string into indiviudal elements
        divided = string.split(",")
        
        #assign values and strip off quotes
        self.source         = divided[2].replace('"', '')
        self.destination    = divided[3].replace('"', '')
        self.protocol       = divided[4].replace('"', '')
        self.bytes          = divided[5].replace('"', '')


#######SORT AND MERGE FUNCTIONS#####
def mySort(data, INDX):
        #1) recursively sort first half of array
        #2) recursively sort second half of array
        #3) merge sorted sublists together

    #get length of data to sort
    length = len(data)

    #verify multiple elements
    if length <= 1: 
        return data

    #recursively break into parts
    left    = mySort(data[:int(length/2)], INDX)
    right   = mySort(data[int(length/2):], INDX)

    #merge halves
    return myMerge(left, right, INDX)

def myMerge(left, right, INDX):
    
    sortedArray = []
    i, j = 0, 0 

    while True: 
            

        #no more elements! time to give up...
        if i == len(left) and j == len(right): 
            break 
    
        #no more elements left from the right
        elif j == len(right):
            sortedArray.append(left[i])
            i += 1
            
        #no more elements left from the left
        elif i == len(left): 
            sortedArray.append(right[j])
            j += 1


        elif int(left[i][INDX]) <= int(right[j][INDX]): 
            sortedArray.append(left[i])
            i += 1

        #right is smaller, so add that one
        else: 
            sortedArray.append(right[j])
            j += 1
    
    return sortedArray




log = PCAP("smallpcap.csv")

print( str(    log.ipsByBytes() ) ) 
print("\n\n")
print( str(    log.ipsByConnections() ) ) 
print("\n\n")
print( str(    log.protocolsByBytes() ) ) 
print("\n\n") 
print( str(    log.protocolsByConnections() ) ) 
print("\n\n")
print( str(    log.connectionsByConnections() ) ) 
print("\n\n")
print( str(    log.connectionsByBytes() ) )

