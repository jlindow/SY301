#
#
#
#
class rotor: 

    def __init__ (self, string):
        self.rotor_list = list(string)
        self.initial = self.rotor_list[0] 
        return 

    def encryptLetter(self, letter):
        position = ( ord(letter) - 65 ) #ASCII 'A' = 65
        return self.rotor_list[position] 

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


class enigma: 

    def __init__ (self, rotor1, rotor2, rotor3):
        
        self.rotor1 = rotor(rotor1) 
        self.rotor2 = rotor(rotor2)
        self.rotor3 = rotor(rotor3)

        return

    def encrypt (self, message):
        r2_count = 1
        r3_count = 1

        messageList = list(message) 
        encryptedMessage = []

        for i in range(len(messageList)):

            rotor1_letter = self.rotor1.encryptLetter(message[i]) 
            if( (r2_count % 27) == 0): 
                self.rotor1.click()


            rotor2_letter = self.rotor2.encryptLetter(rotor1_letter)
            if ( (r3_count % 27) == 0):
                self.rotor2.click()
                r2_count += 1
                

            rotor3_letter = self.rotor3.encryptLetter(rotor2_letter) 
            self.rotor3.click()
            r3_count += 1

            encryptedMessage.append(rotor3_letter)
    
        encryptedMessage = ''.join(encryptedMessage)

        return encryptedMessage

    def decrypt (self, message): 
        r2_count = 1
        r3_count = 1

        messageList = list(message) 
        decryptedMessage = []

        #reset rotors
        self.reset()


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

        return decryptedMessage


    def reset (self): 

        r1 = False
        r2 = False
        r3 = False

        while (r1 == False): 
            r1 = self.rotor1.click()
        while (r2 == False): 
            r2 = self.rotor2.click()
        while (r3 == False): 
            r3 = self.rotor3.click()

        return 

message = "OQMTANMGPABQSDAKAUFXXGJBSPHBZXHLXMBNOHTNQZQGDBMIQNZJ"
e = enigma("SHBMFWEIQRODTAVXCPYZUJKGNL", "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK")

print("\n\nInitial Message: " + message)
print("\nDecrypted Message: " + str(e.decrypt(message)))






