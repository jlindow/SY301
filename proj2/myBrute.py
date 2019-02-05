###################################################
#           MIDN Jacob A. Lindow                  #
#               SY301 - 9991                      #
#                                                 #
#            Dr. Travis Mayberry                  #
#               Project #2                        #
#               4 Feb 2019                        #
###################################################

#Usage: $ python3 myBrute.py shorthashedRockyou.txt shadow.txt output.txt


import sys 

#Read Hash/Password Pairs from shorthashedRockyou.txt (HASH  PASSWORD)
with open(sys.argv[1], 'r') as passwordFile: 
    
    #Initialize an array for our hashtable
    pswdArray = [0] * 20000000 #(Arbitrarily chosen as some large-ish number)
    
    #iterate line by line through password - hash pair file
    for line in passwordFile: 
        
        #Get hash - password pair from line in file
        pswdPair    = line.strip().split()
        
        #Convert Hash Value to an INDEX
        index       = int(pswdPair[0], 16) % len(pswdArray)
        
        #Verify open spot at index
        #Otherwise go find the next open spot
        while True: 
            if ( pswdArray[index] == 0):
                pswdArray[index] = pswdPair
                break 
            else: 
                 index += 1

#Open output.txt file for writing
output = open(sys.argv[3], 'w')


#Read Username/Hash Pairs from shadowFile (USERNAME   HASH) 
with open(sys.argv[2], 'r') as usernameFile: 
   
    #Iterate line by line through username - hash pair file
    for line in usernameFile: 

        #grab username - hash pair from line in file
        usrPair     = line.strip().split()

        #convert hash to an index to perform lookup
        index       = int(usrPair[1], 16) % len(pswdArray)

        #Go get the password at that index
        #Verify hash equals the expected hash, otherwise go find password 
        while True: 
            #first element of pswdPair within pswdArray is the HASH
            if pswdArray[index][0] == usrPair[1]:
                password = pswdArray[index][1]  
                break
            else: 
                index += 1

        #write usrname + pswd to output file: 
        output.write(usrPair[0] + " " + password + "\n")
        print(usrPair[0] + " " + password + "\n")

#close output file
output.close()
