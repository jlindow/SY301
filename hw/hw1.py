#           HW 1
#      MIDN 2/C Lindow
#         1 Oct 18
#   
#     Dr. Travis Mayberry
#        USNA SY301
#

def sortFunc(int1, int2, int3):
    
    #because I dislike bubble sort, and there's only 3 numbers
    num1 = min(int1, int2, int3); 
    num3 = max(int1, int2, int3);
    num2 = (int1 + int2 + int3) - (num1 + num3)

    sorted_list = [num1, num2, num3]

    return sorted_list 

#def everyother_cheating(some_list):
#    odd_list = del some_list[1::2]
#    return odd_list

def everyother(some_list):

    new_list = []
    i        = 0
    
    while (i < len(some_list)):

        if (i % 2) == 0:
            new_list.append(some_list[i])

        i += 1
    
    return new_list


#
# end of file
#
