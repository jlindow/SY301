#
#     Long Live Alan Turing
#      Author: J. Lindow
#
#       SY301 Project 1
#     Dr. Travis Mayberry
#
#

import sys

def attempt():

    plaintext = str(enigma.decrypt(message))

    if ( (plaintext.find("ONE") != -1) and (plaintext.find("MINE") != -1) ): 
    
        return plaintext

    else: 
        return False


class enigma: 

    def __init__ (self, rotor1, rotor2, rotor3):

        self.rotor1 = rotor(rotor1) 
        self.rotor2 = rotor(rotor2)
        self.rotor3 = rotor(rotor3)

        return

    def decrypt (self, message): 
        r2_count = 1
        r3_count = 1

        rotor1_original = self.rotor1 
        rotor2_original = self.rotor2
        rotor3_original = self.rotor3

        messageList = list(message) 
        decryptedMessage = []

        for i in range(len(messageList)): 

            letter = messageList[i]

            rotor3_letter = self.rotor3.decryptLetter(letter) 
            self.rotor3.click() 
            r3_count += 1 

            rotor2_letter = self.rotor2.decryptLetter(rotor3_letter) 
            if ( (r3_count % 27) == 0):
                self.rotor2.click()
                r2_count += 1

            rotor1_letter = self.rotor1.decryptLetter(rotor2_letter)
            if ( (r2_count % 27) == 0): 
                self.rotor1.click()

            decryptedMessage.append(rotor1_letter)

        decryptedMessage = ''.join(decryptedMessage)

        #reset rotors to the way they were when passed
        self.rotor1 = rotor1_original
        self.rotor2 = rotor2_original
        self.rotor3 = rotor3_original

        return decryptedMessage


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



#get rotors and message from command line
message         = sys.argv[1] 
rotor1_initial  = sys.argv[2] 
rotor2_initial  = sys.argv[3] 
rotor3_initial  = sys.argv[4]

#create a machine
enigma = enigma(rotor1_initial, rotor2_initial, rotor3_initial)

rot3_count = 1
rot2_count = 1
rot1_count = 1

################################################################################
################################################################################


while True:

    #attempt to decrypt
    result = attempt()

    if (result == False): 
        #rotor3 clicks everytime
        enigma.rotor3.click()
        rot3_count += 1

        #rotor2 clicks every 26 times    
        if ( (rot3_count % 27) == 0):
            enigma.rotor2.click()
            rot2_count += 1

        #rotor1 clicks every 26 times rotor2 does
        if ( (rot2_count % 27) == 0): 
            enigma.rotor1.click()
            rot1_count += 1

        #after rotor1 clicks 26 times, swap rotors.
        if ( (rot1_count % 27) == 0): 
                #swap order of rotors
                tmp1 = enigma.rotor1
                tmp2 = enigma.rotor2 
                tmp3 = enigma.rotor3

                enigma.rotor1 = tmp3
                enigma.rotor2 = tmp1 
                enigma.rotor3 = tmp2  

    else: 
        print("\n" + result + "\n")
        break

################################################################################    
#
#
# End of Program
#
#
