class Process:

    def __init__ (self, string, num):
        self.name        = string
        self.memoryReq   = num

    def __str__ (self):
        return self.name + ": " + str(self.memoryReq) + "KB" 

class Machine: 
    def __init__ (self, string, num):
        self.name        = string
        self.processList = []
        self.totalMem    = num

    def __str__ (self):
        big_string = self.name + ", " + str(totalMem) + "KB" + "\n\t"
        i = 0
        while i < len(self.processList):
            big_string += "\n"+ self.processList[i].name + ": " + str(self.processList[i].memoryReq) + "KB"
        return (big_string)

    def addProcess(self, process): 
        self.processList.append(process)
    
    def availableMemory(self):
        i = 0
        total_mem_req = 0

        while i < len(self.processList):
            total_mem_req += self.processList[i].memoryReq
            i += 1

        return (self.totalMem - total_mem_req)


    
