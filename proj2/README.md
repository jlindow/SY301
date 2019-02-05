MIDN Jacob A. Lindow
Alpha: 203618
SY301 - Project 2


Task: 
1. This program takes two inputs - a shadowfile containing username and hashes, and a password file containing hashes and passwords. 
2. This program will output a plaintext file containing username and password pairs. 

Implementation: 
1. Files are generated using a python script: 
	$ python3 pwPageGenerator.py rockyouwithcount.txt 5000 shadow.txt answers.txt. 

2. This will result in the generation of shadow.txt, that will contain username - hash pairs. 

3. The hash/password pairs have been precomputed, and are stored in the file hashedRockYou.txt

4. Step 1: Hashtable Generation
	- Execution : $ python3 brute.py hashedRockYou.txt shadow.txt 
 
	- read hash/password pairs from hashedRockYou.txt 
	- for each hash/password pair, convert hash value to an integer index.  
		> index = int(hash, 16) % length(pswdArray) 

	- store password & hash as a tuple at this index
		> password_pair = (hash, password)
		> pswdArray[index] = password_pair
	
	- COLLISION! In the event of a collision (check before trying to 
		     store password there), store the password at the next 
		     available open index. 
 
	- complete these steps for every hash/password pair in the hashedRockYou.txt
 
5. Step 2: Matching usernames and passwords

	- iterate line by line through shadow.txt
	- read username/hash pair into a two element array

		> with open(shadow.txt) as sf: 
			for line in sf: 
				pair = line.strip().split(" ")

	- perform hashtable look up for each username/hash pair. 
		> index    = int(hash, 16) % length(pswdArray)
		  
	- Check value of hash to ensure index is for the correct password (collision detection) 
		  
		> if hash  = pswdArray[index][0]: //pswdArray contains tuples, where tuple[0] is the hash
			password = pswdArray[index]
		  else: 
			//Go knock on the neighbors and find the index
			while (pswdArray[index][0] != hash): 
				index += 1
		
	
	- write to output.txt, usr and password. 
		> with open(output.txt) as out: 
			out.write(usr + " " + password)		
			
	- Complete these steps while iterating through every line of shadow.txt, 
	  and writing to output.txt as username/password pairs are found






		
