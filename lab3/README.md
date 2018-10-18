1. What do you think is the runtime of a single append function call in cArray? Why?

      A single apend function call in cArray requires the creation of a new array and the copying of "n" elements into said new array. The runtime for such a functional call is dependent upon the number of elements, n, in the array and therefore is simply linear and   equal to O(n). 


2. What do you think is the runtime of a single append function call in cArray5? Why?
      Similarly, cArray5 is also only dependent upon the number of elements in the array, and is therefore also  linear with a run    time of O(n). The difference with cArray5 is that the total runtime of the program is faster, because the append function is called  five times less frequently. However, the actual run time of a single append function call remains the same. 


3. What do you think is the runtime of a single append function call in cList? Why? 
      Like in cArray5, the runtime of the entire program is significantly faster because the append function is called exponentially less frequently. However, the run time of a single append function call is still the same. Regardless how much larger we make the new array, the actual run time is only dependent on how many elements we have to copy into the new array, and changes linearly as the     number of elements in the array changes. Therefore, the runtime of a single append call is still only O(n).  


4. Which of the two approaches in C do you think is actually used to implement the append function in Python? Why?
      I would assume that append function in Python is more similar to cList, considering it is a highly optimized language with    dynamically allocated memory. I don't exactly know what happends behind the scense when Python resizes memory to append an array, but I would certainly assume that Python resizes the array for larger than is actually necessary for the data to be added. I also assume Python's memory re-allocation algorithims are slightly more complicated than simply doubling the size of an array every time an append is necessary, but the specifics of such an optimization algorithim are far beyond my knowledge. 


5. Python's lists also have an insert function, which inserts an element in the middle of the list. 
   Given the implementation you think is most likely, what do you believe would be the runtime of this insert function? 
   Why? Your explanation should say what operations would have to be performed on the array during an insert. 
   AFTER you've thought about these questions, replace the append line in pylist.py with array.insert(len(arra)//2).
   
   The run time for a python insert should be O(n) because it is entirely dependent upon the number of elements in the list which linearly affects run time. In order to insert an element in the middle of a list, an effectively new list has to be created one element larger than the previous. The old list has to iterated through and copied into the new list up into the desired insertion point, the new item added, and the remainder of the old list copied into the new. The copying of these elements linearlly affects runtime as the number of elements in the list changes. 
      
