#
#         Lab 1 
#     MIDN 2/C Lindow
#
#         SY301
#   Dr. Travis Mayberry
#

class Adding: 

    def __init__(self, int1, int2): 
        self.int1 = int1
        self.int2 = int2

    def addEm(self, newint):
        return self.int1 + self.int2 + newint

    def __str__(self): 
        return "Adding (" + str(self.int1) +  ", " + str(self.int2) + ")"

