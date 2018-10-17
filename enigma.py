#
#
#
#


class rotor: 

    def __init__ (self, string):
        self.rotor_list = string2list(string) #CONVERTS A STRING TO LIST OF LETTERS
        return 0 

    def encryptLetter(self, letter):
        position = alpha2position(letter) #converts a char to an int 1-25 (position in alphabet)
        encrypted_letter = rotor_list[position] #returns matching char from rotor list
        return encrypted_letter

    def decryptLetter(self, letter): 
        position = self.rotor_list.index(letter) #determine index within rotor list
        decrypted_letter = position2alpha(position) #convert an int to corresponding char in alphabet
        return decrypted_letter

    def click(self)
        #ROTATE rotor_list ONE CLICK
        self.rotor_list = self.rotor_list[1:] + self.rotor_list[:1]
