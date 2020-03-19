# This program outputs the reversal of the given input string

from math import *


# function that joins the given array of characters into a 
def convert(str):

    s = ""

    return(s.join(str))



str = list(input("Enter the string that has to be reversed : \n"))

i = 0           # Number of steps taken to get reverse of the given string
len = len(str)  # Length of the given string

# Loop Invariant : Characters in str[i,...,len-i-1] are the same as in the given string 

while(i < floor(len/2)):
        str[i], str[len-i-1] = str[len-i-1], str[i]             # To make progress
        i = i+1                                                 # To maintain the definition of i
        print(str)


print("Reversal of the given string is : \n", convert(str))
