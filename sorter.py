#
#       HW1 - Part 1
#      Sorter Program
#        3 Oct 18
#
#    Dr. Travis Mayberry 
#         SY301
#

import sys

print('This program will sort three numbers\n')

while True: 

    try: 
        print('Please enter the first number: ') 
        int1 = int(input())

    except ValueError: 
        print('Not an int...') 
        continue

    if int1 == "": 
        print('You have to enter something...')
        continue

    else: 
        break

while True: 

    try: 
        print('Please enter the second number: ') 
        int2 = int(input())

    except ValueError: 
        print('Not an int...') 
        continue

    if int2 == "": 
        print('You have to enter something...')
        continue

    else: 
        break


while True: 

    try: 
        print('Please enter the third number: ') 
        int3 = int(input())

    except ValueError: 
        print('Not an int...') 
        continue

    if int3 == "": 
        print('You have to enter something...')
        continue

    else: 
        break


maxint = max(int1, int2, int3)
minint = min(int1, int2, int3)
midint = (int1 + int2 + int3) - (maxint + minint)

print('Sorted: ' + str(minint) + ',' + str(midint) + ',' + str(maxint)) 



