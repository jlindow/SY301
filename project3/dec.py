#!/usr/bin/python

#################################################################################
#   Public - Private Key Decryption                                             #                                   
#   Author: Jacob A. Lindow                                                     #                      
#                                                                               #
#   SY301 - Project 3                                                           # 
#                                                                               #
#################################################################################
#################################################################################
# Usage: $ python3 dec.py private.txt message.txt                               #
#                                                                               #
# Functionality:                                                                #
#       1) Read Private Key into an array                                       #
#       2) Read Message line by line, splitting at delimiter into an array      #
#       3) Check if first element matches ANY element of PrivKeyArray           #
#       4) If so, take second element (number) and add to sum                   #
#       5) Continue for every line of the message                               #
#       6) Finally, convert sum fron int to string                              #
#################################################################################

import sys

# Variable Declarations 
cipherSum = 0
privateKey = [] 

# Read Private Key into an array 
with open(sys.argv[1], 'r') as pkFile: 
    for line in pkFile: 
        privateKey.append(line.rstrip())

# Read Message and check node names against private key 
with open(sys.argv[2], 'r') as msg: 
    for line in msg: 
        msgLine = line.split() 
        if msgLine[0].rstrip() in privateKey: 
            cipherSum += int(msgLine[1].rstrip())

# Convert cipherSum to a string 
b           = cipherSum.to_bytes( (cipherSum.bit_length() // 8) + 1 , byteorder = 'big')
plainText   = b.decode('ascii') 

print("Plaintext Message: " + plainText + "\n")
