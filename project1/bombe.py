#
#     Long Live Alan Turing
#      Author: J. Lindow
#
#       SY301 Project 1
#     Dr. Travis Mayberry
#
#

import sys

def attempt(rotor1, rotor2, rotor3):

    e = enigma(rotor1, rotor2, rotor3)

    #print("Rotor1: " + str(rotor1.rotor_list)) 
    #print("Rotor2: " + str(rotor2.rotor_list)) 
    #print("Rotor3: " + str(rotor3.rotor_list) + "\n") 

    plaintext = str(e.decrypt(message))

    if ( "MINE" in plaintext and "WALKING" in plaintext): 
 
        print("\n MATCH FOUND: ") 
        print(plaintext)
        sys.exit(0)
        return True

    else: 
        return False


class enigma: 

    def __init__ (self, rotor1, rotor2, rotor3):

        self.r1 = rotor(rotor1)
        self.r2 = rotor(rotor2)
        self.r3 = rotor(rotor3)

        return

    def decrypt (self, message): 

        #print("Rotor2 Before Decrypt:" + str(rotor2.rotor_list))
        #print("Rotor3 Before Decrypt: " + str(rotor3.rotor_list))
        #print("\n")

        r2_count = 1
        r3_count = 1

        messageList = list(message) 
        decryptedMessage = []

        for i in range(len(messageList)): 

            letter = messageList[i]

            rotor3_letter = self.r3.decryptLetter(letter) 
            self.r3.click() 
            r3_count += 1 

            rotor2_letter = self.r2.decryptLetter(rotor3_letter) 
            if ( (r3_count % 27) == 0):
                self.r2.click()
                r2_count += 1

            rotor1_letter = self.r1.decryptLetter(rotor2_letter)
            if ( (r2_count % 27) == 0): 
                self.r1.click()

            decryptedMessage.append(rotor1_letter)

        decryptedMessage = ''.join(decryptedMessage)


        #print("Rotor2 AFTER: " + str(rotor2.rotor_list))
        #print("Rotor3 AFTER: "  + str(rotor3.rotor_list))
        #print("\n")

        return str(decryptedMessage)
class rotor: 

    def __init__ (self, string):
        self.rotor_list = list(string)
        self.initial = self.rotor_list[0] 
        return

    def decryptLetter(self, letter): 
        position = self.rotor_list.index(letter) #get index of encoded letter
        letter = chr(position + 65) #find letter in alphabet at that index
        return (letter)

    def click(self):
        self.rotor_list = self.rotor_list[1:] + self.rotor_list[:1]
        if (self.initial == self.rotor_list[0]): 
            return True 
        else: 
            return False 

def shift(string): 
    stringList = list(string)
    shiftedList = stringList[1:] + stringList[:1]
    shiftedString = ''.join(shiftedList)
    return shiftedString


#get rotors and message from command line
message         = sys.argv[1] 
rotor1          = sys.argv[2]
rotor2          = sys.argv[3]
rotor3          = sys.argv[4]

count = 0
swapCount = 0

################################################################################
################################################################################

while True:

    #attempt to decrypt
    print("Rotor1: " + rotor1)
    print("Rotor2: " + rotor2)
    print("Rotor3: " + rotor3 + "\n")

    result = attempt(rotor1, rotor2, rotor3)
    count += 1    

    if (count > 105456): 
        print("Mission Failed.")
        break

    if (result == False): 
        #rotor3 clicks everytime
        rotor3 = shift(rotor3)
        print("SHIFT3, " + str(count))

        #rotor2 clicks every 26 times    
        if ( (count) % 26 == 0):
            rotor2 = shift(rotor2)
            print("SHIFT2, " + str(count))

        #rotor1 clicks every 26 times rotor2 does
        if ( (count) % 676 == 0):
            rotor1 = shift(rotor1)
            print("SHIFT1, " + str(count))
    
        #after rotor1 clicks 26 times, swap rotors.
        if ( (count) % 17576 == 0):
            if (swapCount == 0): #ACB
                tmp = rotor2
                rotor2 = rotor3
                rotor3 = tmp
                print("Swap 1")
    
            if (swapCount == 1): #BCA
                tmp = rotor3
                rotor3 = rotor1 
                rotor1 = tmp
                print("Swap 2")

            if (swapCount == 2): #BAC
                tmp = rotor2
                rotor2 = rotor3
                rotor3 = tmp
                print("Swap 3")
    
            if (swapCount == 3): #CAB
                tmp = rotor1 
                rotor1 = rotor3 
                rotor3 = tmp
                print("Swap 4")
    
            if (swapCount == 4): #CBA
                tmp = rotor2 
                rotor2 = rotor3
                rotor3 = tmp
                print("Final swap.")
            
            swapCount += 1
    else: 
        print("\n" + str(result) + "\n")
        break

################################################################################    
#
#
# End of Program
#
#
